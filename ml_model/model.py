from ultralytics import YOLO
import os

class ModelManager:
    def __init__(self, model_path="yolov8n.pt"):
        self.model_path = model_path

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"❌ Model not found at: {self.model_path}")
        return YOLO(self.model_path)

    def save_model(self, model, save_path="trained_model.pt"):
        model.save(save_path)
        print(f"✅ Model saved to {save_path}")
