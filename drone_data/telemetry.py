import random
from datetime import datetime

class TelemetryFetcher:
    def __init__(self, test_mode=True):
        self.test_mode = test_mode

    def get_data(self):
        if self.test_mode:
            return {
                "gps": {"lat": 19.123456 + random.uniform(-0.001,0.001),
                        "lon": 73.987654 + random.uniform(-0.001,0.001),
                        "altitude_m": random.uniform(10,50)},
                "battery": random.uniform(50,100),
                "timestamp": datetime.utcnow().isoformat()
            }
        else:
            raise NotImplementedError