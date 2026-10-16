
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

    # Converts property of pixel color to hue, saturation, lightness
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define colors to extract
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Portion of image or frame
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Applying mask to original image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display mask compared to frame
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    ### <<< CAN USE THIS TO CONVERT USER-DEFINED COLORS AS NEEDED: >>> ###
    # BGR_color = np.array([[[255, 0, 0]]])
    # x = (cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV))
    # x[0][0]

    # Shows frame as predetermined image
    cv2.imshow('frame', result)
# After 1 milisecond, closes webcam if key pressed is 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
