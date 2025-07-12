import cv2

class CameraStream:
    def __init__(self, camera_id=0, width=1280, height=720):
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("❌ Cannot read frame from camera.")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
