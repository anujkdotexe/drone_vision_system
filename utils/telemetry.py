import random
from datetime import datetime

class TelemetryFetcher:
    def __init__(self, test_mode=True):
        self.test_mode = test_mode

    def get_data(self):
        if self.test_mode:
            return {
                "gps": {
                    "lat": round(19.123456 + random.uniform(-0.001, 0.001), 6),
                    "lon": round(73.987654 + random.uniform(-0.001, 0.001), 6),
                    "altitude_m": round(random.uniform(10.0, 30.0), 2)
                },
                "battery": round(random.uniform(60, 100), 1),
                "timestamp": datetime.utcnow().isoformat()
            }
        else:
            # Future: Add SDK calls to actual drone GPS/battery sensors
            raise NotImplementedError("Real telemetry not yet integrated.")
