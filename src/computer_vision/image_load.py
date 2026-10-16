
# Import path for file-path reliability
# Import OpenCV for image processing
from pathlib import Path
import cv2

# Build path to test image relative to file; must be PNG or JPEG
image_path = Path(__file__).parent / "assets" / "tesseract.jpg"

# Load image (-1 = unchanged, 0 = grayscale, 1 = color)
img = cv2.imread(str(image_path), 1)
# Resize image by pixels
img = cv2.resize(img, (400, 400))

### <<< CAN USE THIS FOR SCALING: >>> ###
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

### <<< CAN USE THIS FOR ROTATION: >>> ###
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# Verify successful image load
if img is None:
    print("Failed to load image:", image_path)
else:
    ### <<< CAN USE THIS TO SAVE IMAGE TO NEW FILE: >>> ###
    # cv2.imwrite('new_img.jpg', img)
    
    cv2.imshow('Image', img)
    # Displays image; waits until key pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
