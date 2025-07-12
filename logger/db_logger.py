from pymongo import MongoClient

class MongoLogger:
    def __init__(self, uri, db, coll):
        self.client=MongoClient(uri); self.col=self.client[db][coll]
    def log(self, entry): self.col.insert_one(entry)