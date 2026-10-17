
from pathlib import Path
import numpy as numpy
import cv2

# Path to YuNet model
base_path = Path(__file__).parent
assets_path = base_path / "assets"

cap = cv2.VideoCapture(0)

### <<< TO USE MP4 VIDEOS: >>> ###
# video_path = assets_path / "big_buck_bunny.mp4"
# cap = cv2.VideoCapture(str(video_path))

# Path to YuNet face detection model
model_path = assets_path / "face_detection_yunet_2026may.onnx"

# Read frame for camera dimensions
ret, frame = cap.read()

if not ret:
    raise RuntimeError("Could not read from camera")

height, width = frame.shape[:2]

# Pretrained YuNet facial detection model
face_detector = cv2.FaceDetectorYN.create(
    model=str(model_path),
    config="",
    input_size=(width, height),
    score_threshold=0.9,
    nms_threshold=0.3,
    top_k=5000
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    height, width = frame.shape[:2]

    # Tell detector current frame size
    face_detector.setInputSize((width, height))

    # Detect faces
    _, faces = face_detector.detect(frame)

    if faces is not None:
        for face in faces:

            # Face bounding box
            x, y, w, h = face[:4].astype(int)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                5
            )

            # YuNet already returns facial landmarks
            landmarks = face[4:14].astype(int).reshape(5, 2)

            # First two landmarks are the eyes
            right_eye = tuple(landmarks[0])
            left_eye = tuple(landmarks[1])

            cv2.circle(frame, right_eye, 5, (255, 0, 0), -1)
            cv2.circle(frame, left_eye, 5, (255, 0, 0), -1)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
