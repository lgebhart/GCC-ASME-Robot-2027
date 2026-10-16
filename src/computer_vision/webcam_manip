
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

    # Passes zeros into frame array of video feed
    image = np.zeros(frame.shape, np.uint8)

    # Resizes frame scaling by width and height
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Copy and paste smaller frames into 4 corners and rotate 4 corners
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    # Shows frame as predetermined image
    cv2.imshow('frame', image)


# After 1 milisecond, closes webcam if key pressed is 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()