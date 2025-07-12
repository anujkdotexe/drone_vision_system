from camera.high_speed_stream import CameraStream
from camera.frame_enhancer import enhance_frame
from drone_data.telemetry import TelemetryFetcher
from ml_model.inference import ObjectDetector
from ml_model.tracker import VisibilityTracker
from logger.db_logger import MongoLogger
from logger.data_logger import DataLogger
from utils.helpers import calc_coverage
from utils.config_loaders import load_config
config = load_config()
import cv2

def main():
    cfg = load_config()
    cam = CameraStream(cfg['camera_id'])
    detector = ObjectDetector(cfg['model_path'])
    telem = TelemetryFetcher(test_mode=True)
    mlogger = MongoLogger(cfg['mongo_uri'], cfg['mongo_db'], cfg['mongo_coll'])
    dlogger = DataLogger(mlogger, telem)
    tracker = VisibilityTracker()

    print("Starting Drone Vision System...")
    try:
        while True:
            frame = cam.read_frame()
            frame = enhance_frame(frame)
            annotated, dets = detector.detect(frame, cfg['conf_thresh'])
            for det in dets:
                det['coverage']=calc_coverage(det['bbox'], frame.shape)
                id = tracker.track(det)
                det['instance_id']=id
                det['duration']=tracker.duration(id)
                dlogger.log(det)
            cv2.imshow("Live", annotated)
            if cv2.waitKey(1)&0xFF==ord('q'): break
    finally:
        cam.release()

if __name__=='__main__': main()