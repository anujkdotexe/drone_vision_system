from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame, conf_thresh=0.3):
        results = self.model.predict(source=frame, conf=conf_thresh, stream=False, verbose=False)
        if not results:
            return frame, []
        annotated = results[0].plot()
        detections = []
        for r in results:
            if r.boxes is None: continue
            for box in r.boxes:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                detections.append({
                    "bbox":(x1,y1,x2,y2),
                    "confidence":float(box.conf),
                    "class_id":int(box.cls),
                    "class_label":self.model.names[int(box.cls)]
                })
        return annotated, detections