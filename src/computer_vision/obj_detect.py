
# Import path for file-path reliability
# Imports NumPy
# Import OpenCV for image processing
from pathlib import Path
import numpy as np
import cv2

# Path to computer_vision folder
base_path = Path(__file__).parent
assets_path = base_path / "assets"

# Build paths to source image and template
image_path = assets_path / "Obstacle_Course.jpg"

# Pulls images as grayscale; must be JPEG or PNG; resizes
img = cv2.imread(str(image_path), cv2.IMREAD_COLOR)

# Verify successful loading
if img is None:
    raise FileNotFoundError(f"Could not load image: (image_path)")

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Declares template types
templates = {
    "large_blue_sphere": "Large_Blue_Sphere.PNG",
    "large_orange_sphere": "Large_Orange_Sphere.PNG",
    "small_blue_cube": "Small_Blue_Cube.PNG",
    "small_blue_cylinder": "Small_Blue_Cylinder.PNG",
    "small_orange_cylinder": "Small_Orange_Cylinder.PNG",
    "rectangular_wall": "Rectangular_Wall.PNG",
}

# Algorithm attribute image template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Specifies searching for all template items
for name, filename in templates.items():
    template_path = assets_path / filename

    template = cv2.imread(
        str(template_path),
        cv2.IMREAD_COLOR
    )

# Verify successful template loading
    if template is None:
        print(f"Could not load template: {template_path}")
        continue

# Resize template
    template = cv2.resize(template, (0, 0), fx=0.9, fy=0.9)

    h, w = template.shape[:2]

    for method in methods:
        img2 = img.copy()

    # Detection confidence

    # Performs convolution; return accuracy
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

    # Draw rectangle around target item; black due to grayscale
        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(img2, location, bottom_right, (0, 255, 0), 5)
        cv2.imshow(name, img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
