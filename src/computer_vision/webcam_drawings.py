
# Imports NumPy
# Import OpenCV for image processing
import numpy as np
import cv2

# Captures chosen webcam
cap = cv2.VideoCapture(0)

# Always returns frame of image
while True:
    ret, frame = cap.read()

    # Gets width and height property of video capture
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Draws on frame in position (x,y), BGR (x, y, z), thickness (x))
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    # Text on frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'ASME 2027 Robot Vision', (10, height -10), font, 0.5, (255, 255, 255), 5, cv2.LINE_AA)

    # Shows frame as predetermined image
    cv2.imshow('frame', img)


# After 1 milisecond, closes webcam if key pressed is 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()