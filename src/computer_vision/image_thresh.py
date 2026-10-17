
# Import path for file-path reliability
# Import OpenCV for image processing
# Import NumPy
# Import Matplotlib for displaying threshold comparisons
from pathlib import Path
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Path to computer_vision folder
base_path = Path(__file__).parent
assets_path = base_path / "assets"


### <<< USE FOR IMAGE IN JPEG OR PNG >>> ###

# Build path to source image
image_path = assets_path / "Obstacle_Course.jpg"

# Load image as grayscale
img = cv.imread(
    str(image_path),
    cv.IMREAD_GRAYSCALE
)

# Verify successful loading
if img is None:
    raise FileNotFoundError(f"Could not load image: {image_path}")

# Blur image
img = cv.medianBlur(img, 5)


# Global threshold
ret, th1 = cv.threshold(
    img,
    127,
    255,
    cv.THRESH_BINARY
)


# Adaptive mean threshold
th2 = cv.adaptiveThreshold(
    img,
    255,
    cv.ADAPTIVE_THRESH_MEAN_C,
    cv.THRESH_BINARY,
    11,
    2
)


# Adaptive Gaussian threshold
th3 = cv.adaptiveThreshold(
    img,
    255,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv.THRESH_BINARY,
    11,
    2
)


# Titles for displayed images
titles = [
    "Original Image",
    "Global Thresholding (v = 127)",
    "Adaptive Mean Thresholding",
    "Adaptive Gaussian Thresholding"
]


# Images to display
images = [
    img,
    th1,
    th2,
    th3
]


# Display threshold comparisons
for i in range(4):

    plt.subplot(2, 2, i + 1)

    plt.imshow(
        images[i],
        "gray"
    )

    plt.title(
        titles[i]
    )

    plt.xticks([])
    plt.yticks([])


plt.show()
