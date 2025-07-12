import time

class VisibilityTracker:
    def __init__(self): self.instances = {}; self.counter=1
    def track(self, det):
        key = (det['class_id'], det['bbox'])
        if key not in self.instances:
            self.instances[key] = {'id':self.counter, 'start':time.time()}
            self.counter +=1
        return self.instances[key]['id']
    def duration(self, inst_id):
        for v in self.instances.values():
            if v['id']==inst_id:
                return round(time.time()-v['start'],2)
        return 0