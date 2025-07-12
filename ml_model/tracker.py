import time

class VisibilityTracker:
    def __init__(self):
        self.instances = {}
        self.next_id = 1

    def track(self, detection):
        key = (detection["class_id"], detection["bbox"])
        if key not in self.instances:
            self.instances[key] = {"id": self.next_id, "start": time.time()}
            self.next_id += 1
        return self.instances[key]["id"]

    def get_visibility_duration(self, instance_id):
        for v in self.instances.values():
            if v["id"] == instance_id:
                return round(time.time() - v["start"], 2)
        return 0
