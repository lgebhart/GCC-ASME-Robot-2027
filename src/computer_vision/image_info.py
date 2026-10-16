
# Import path for file-path reliability
# Import OpenCV for image processing
# Import random
from pathlib import Path# Import OpenCV for image processing
import cv2
import random

# Build path to test image relative to file; must be PNG or JPEG
image_path = Path(__file__).parent / "assets" / "tesseract.jpg"

# Load image (-1 = unchanged, 0 = grayscale, 1 = color)
img = cv2.imread(str(image_path), 1)

### <<< CAN USE TO DISPLAY IMAGE INFO: >>> ###
# print(img)

### <<< CAN USE TO DISPLAY IMAGE TYPE: >>> ###
# print(type(img))

### <<< CAN USE TO PRINT IMAGE FIRST ROW COLORS (BGR): >>> ###
# print(img[257][45:400])

### <<< CAN USE TO PRINT SHAPE OF NUMPY ARRAY: >>> ###
# print(img.shape)

### <<< CAN CHANGE SECTION OF IMAGE TO RANDOM COLORS >>> ###
# for i in range(100):
    # for j in range(img.shape[1]):
        # img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

### <<< CAN COPY FROM IMAGE SECTION AND PASTE INTO IMAGE >>> ###
# tag = img[200:400, 300:500]
# img[100:300, 250:450] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
