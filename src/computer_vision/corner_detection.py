
# Import path for file-path reliability
# Imports NumPy
# Import OpenCV for image processing
from pathlib import Path
import numpy as np
import cv2

# Path to computer_vision folder
base_path = Path(__file__).parent
assets_path = base_path / "assets"

# Open webcam
cap = cv2.VideoCapture(0)

# Verify webcam opened
if not cap.isOpened():
    raise RuntimeError("Could not open webcam")

while True:

    # Read frame from webcam
    ret, img = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Resize image
    img = cv2.resize(img, (0, 0), fx=0.80, fy=0.80)

    # Convert to grayscale for algorithm shape detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Corner detection algorithm by image, num points, min quality, and min euclidean distance
    corners = cv2.goodFeaturesToTrack(gray, 300, 0.0001, 10)

    # Only process if corners are detected
    if corners is not None:

        # Convert corners to integers
        corners = corners.astype(int)

        # Display corners to screen
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

        # For 2D space (Pythagorean Theorem):
        # (x1, y1) (x2, y2)
        # sqrt((x2 - x1)^2 + (y2 - y1)^2)

        # Maximum distance between points
        max_distance = 25

        # Draw red colored lines between near-points for barriers
        for i in range(len(corners)):
            for j in range(i + 1, len(corners)):
                x1, y1 = corners[i].ravel()
                x2, y2 = corners[j].ravel()

                # Calculate Euclidean distance
                distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                # Connect near-points
                if distance <= max_distance:
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Create blank avoidance mask
        avoidance_mask = np.zeros_like(gray)

        # Adjustable avoidance radius
        avoidance_radius = 10

        # Fill space around every detected corner
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

    # Display live frame
    cv2.imshow('Frame', img)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()