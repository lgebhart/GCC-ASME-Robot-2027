
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

# 1. Can use to display image info:
# print(img)

# 2. Can use to display image type:
# print(type(img))

# 3. Can use to print image first row colors (BGR)
# print(img[257][45:400])

# 4. Can use to print shape of NumPy Array:
# print(img.shape)

# 5. Can change section of image to random colors
# for i in range(100):
    # for j in range(img.shape[1]):
        # img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 6. Can copy from image section and paste into image
# tag = img[200:400, 300:500]
# img[100:300, 250:450] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
