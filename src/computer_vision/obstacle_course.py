# Import path for file-path reliability
# Imports NumPy
# Import OpenCV for image processing
from pathlib import Path
import numpy as np
import cv2

# Path to computer_vision folder
base_path = Path(__file__).parent
assets_path = base_path / "assets"

# Path to beanbag template
beanbag_path = assets_path / "beanbag.png"

# Path to pencil template
pencil_path = assets_path / "pencil.png"

### BEANBAG TEMPLATE ###
beanbag_template = cv2.imread(str(beanbag_path), cv2.IMREAD_COLOR)

# Verify successful template loading
if beanbag_template is None:
    raise FileNotFoundError(f"Could not load template: {beanbag_path}")

# Resize template to match resized image
beanbag_template = cv2.resize(beanbag_template, (0, 0), fx=0.9, fy=0.9)

# Get beanbag template dimensions
beanbag_h, beanbag_w = beanbag_template.shape[:2]

### PENCIL TEMPLATE ###
pencil_template = cv2.imread(str(pencil_path), cv2.IMREAD_COLOR)

if pencil_template is None:
    raise FileNotFoundError(f"Could not load template: {pencil_path}")

pencil_template = cv2.resize(pencil_template, (0, 0), fx=0.80, fy=0.80)
pencil_h, pencil_w = pencil_template.shape[:2]

# Open the Jetson CSI camera
pipeline = (
    "nvarguscamerasrc sensor-id=0 ! "
    "video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, "
    "format=(string)NV12, framerate=(fraction)30/1 ! "
    "nvvidconv ! "
    "video/x-raw, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! "
    "appsink drop=true max-buffers=1 sync=false"
)

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    raise RuntimeError("Could not open the Jetson CSI camera")

while True:

    # Read frame from Jetson CSI camera
    ret, img = cap.read()

    if not ret:
        print("Could not read camera frame")
        break

    # Resize image
    img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

    ### <<< BEANBAG DETECTION >>> ###
    beanbag_result = cv2.matchTemplate(
        img,
        beanbag_template,
        cv2.TM_CCOEFF_NORMED
    )

    beanbag_min_val, beanbag_max_val, beanbag_min_loc, beanbag_max_loc = cv2.minMaxLoc(beanbag_result)
    print("Beanbag confidence:", beanbag_max_val)
    beanbag_detected = beanbag_max_val >= 0.50

    if beanbag_detected:
        beanbag_location = beanbag_max_loc
        beanbag_bottom_right = (
            beanbag_location[0] + beanbag_w,
            beanbag_location[1] + beanbag_h
        )

        # Draw green rectangle around beanbag
        cv2.rectangle(img, beanbag_location, beanbag_bottom_right, (0, 255, 0), 5)

    ### <<< PENCIL DETECTION >>> ###
    pencil_result = cv2.matchTemplate(
        img,
        pencil_template,
        cv2.TM_CCOEFF_NORMED
    )

    pencil_min_val, pencil_max_val, pencil_min_loc, pencil_max_loc = cv2.minMaxLoc(pencil_result)
    print("Pencil confidence:", pencil_max_val)
    pencil_detected = pencil_max_val >= 0.70

    if pencil_detected:
        pencil_location = pencil_max_loc
        pencil_bottom_right = (
            pencil_location[0] + pencil_w,
            pencil_location[1] + pencil_h
        )

        # Draw green rectangle around pencil
        cv2.rectangle(img, pencil_location, pencil_bottom_right, (0, 255, 0), 5)

    ### <<< CORNER DETECTION >>> ###

    # Convert to grayscale for algorithm shape detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Corner detection algorithm by image, num corners, min quality, and min euclidean distance
    corners = cv2.goodFeaturesToTrack(
        gray,
        maxCorners=300,
        qualityLevel=0.01,
        minDistance=10
    )

    # Create blank avoidance mask
    avoidance_mask = np.zeros_like(gray)

    # Adjustable avoidance radius
    avoidance_radius = 10

    # Only process if corners are detected
    if corners is not None:

        # Display corners to screen
        corners = corners.astype(int)

        for corner in corners:
            x, y = corner.ravel()

            # Skip corner points inside beanbag box
            if beanbag_detected:
                if (
                    beanbag_location[0] <= x <= beanbag_bottom_right[0]
                    and
                    beanbag_location[1] <= y <= beanbag_bottom_right[1]
                ):
                    continue

            # Skip pencil area
            if pencil_detected:
                if (
                    pencil_location[0] <= x <= pencil_bottom_right[0]
                    and
                    pencil_location[1] <= y <= pencil_bottom_right[1]
                ):
                    continue

            cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

        # For 2D space (Pythagorean Theorem):
        # (x1, y1) (x2, y2)
        # sqrt((x2 - x1)^2 + (y2 - y1)^2)

        # Maximum distance between points
        max_distance = 20

        # Draw red colored lines between near-points for barriers
        for i in range(len(corners)):
            for j in range(i + 1, len(corners)):
                x1, y1 = corners[i].ravel()
                x2, y2 = corners[j].ravel()

                # Calculate Euclidean distance
                distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                # Connect near-points
                if distance <= max_distance:

                    # Skip lines connected to beanbag
                    if beanbag_detected:

                        point1_in_beanbag = (
                            beanbag_location[0] <= x1 <= beanbag_bottom_right[0]
                            and
                            beanbag_location[1] <= y1 <= beanbag_bottom_right[1]
                        )

                        point2_in_beanbag = (
                            beanbag_location[0] <= x2 <= beanbag_bottom_right[0]
                            and
                            beanbag_location[1] <= y2 <= beanbag_bottom_right[1]
                        )

                        if point1_in_beanbag or point2_in_beanbag:
                            continue

                    # Skip lines connected to pencil
                    if pencil_detected:
                        point1_in_pencil = (
                            pencil_location[0] <= x1 <= pencil_bottom_right[0]
                            and
                            pencil_location[1] <= y1 <= pencil_bottom_right[1]
                        )

                        point2_in_pencil = (
                            pencil_location[0] <= x2 <= pencil_bottom_right[0]
                            and
                            pencil_location[1] <= y2 <= pencil_bottom_right[1]
                        )

                        if point1_in_pencil or point2_in_pencil:
                            continue

                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Fill space around every detected corner
        for corner in corners:
            x, y = corner.ravel()

            # Skip beanbag area
            if beanbag_detected:
                if (
                    beanbag_location[0] <= x <= beanbag_bottom_right[0]
                    and
                    beanbag_location[1] <= y <= beanbag_bottom_right[1]
                ):
                    continue

            # Skip pencil area
            if pencil_detected:
                if (
                    pencil_location[0] <= x <= pencil_bottom_right[0]
                    and
                    pencil_location[1] <= y <= pencil_bottom_right[1]
                ):
                    continue

            cv2.circle(img, (x, y), 4, (0, 0, 255), -1)
            cv2.circle(avoidance_mask, (x, y), avoidance_radius, 255, -1)

    # Display frame
    cv2.imshow("Frame", img)

    ### <<< CAMERA CONTROLS >>> ###

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()

# Close OpenCV windows
cv2.destroyAllWindows()