
# Import path for file-path reliability
# Import OpenCV for image processing
from pathlib import Path
import cv2

# Build path to test image relative to file; must be JPG
image_path = Path(__file__).parent / "assets" / "tesseract.jpg"

# Load image in grayscale
img = cv2.imread(str(image_path), 0)

# Verify successful image load
if img is None:
    print("Failed to load image:", image_path)
else:
    # Displays image; waits until key pressed
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
