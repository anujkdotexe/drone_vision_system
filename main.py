from ml_model.inference import ObjectDetector
import cv2

# Create the YOLOv8 detector object
detector = ObjectDetector(model_path="yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    annotated_frame, detections = detector.detect(frame)

    # Show annotated output
    cv2.imshow("YOLOv8 Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
