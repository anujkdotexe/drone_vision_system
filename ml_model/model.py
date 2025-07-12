from ultralytics import YOLO
import os

class ModelManager:
    def __init__(self, model_path):
        self.model_path = model_path
    def load(self):
        return YOLO(self.model_path)
    def save(self, model, out_path):
        model.save(out_path)