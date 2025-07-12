class DataLogger:
    def __init__(self, mongo_logger, telemetry):
        self.mongo = mongo_logger; self.telemetry = telemetry
    def log(self, det):
        record = det.copy()
        record.update(self.telemetry.get_data())
        self.mongo.log(record)