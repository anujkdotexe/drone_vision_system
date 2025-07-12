from pymongo import MongoClient

class MongoLogger:
    def __init__(self, uri="mongodb://localhost:27017", db_name="drone_vision", collection="detections"):
        self.client = MongoClient(uri)
        self.collection = self.client[db_name][collection]

    def log_detection(self, data):
        self.collection.insert_one(data)
