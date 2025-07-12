# drone_vision_system/ml_model/inference.py

from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model.predict(source=frame, stream=False, verbose=False)

        if not results:
            return frame, []

        detections = []
        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf)
                cls = int(box.cls)
                detections.append({
                    "bbox": (x1, y1, x2, y2),
                    "confidence": conf,
                    "class_id": cls,
                    "class_label": self.model.names[cls]
                })

        annotated = results[0].plot()
        return annotated, detections
