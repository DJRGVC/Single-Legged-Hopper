import os
import random
from PIL import Image, ImageDraw
import pytesseract

# Define path to the directory containing images
images_path = '../raw_data/images'

# Get a list of all image files in the directory
all_images = [img for img in os.listdir(images_path) if img.endswith('.png') or img.endswith('.jpg')]

# Select a random image
image_name = random.choice(all_images)
img_path = os.path.join(images_path, image_name)

# Load the random image
img = Image.open(img_path)

# Convert to grayscale
gray = img.convert('L')

# Perform OCR
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

# Create a draw object
draw = ImageDraw.Draw(img)

# Draw bounding boxes for each detected word with confidence > 0
for i in range(len(data['text'])):
    if int(data['conf'][i]) > 0:  # Check confidence level
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        draw.rectangle([x, y, x + w, y + h], outline='green', width=2)

# Display the image with bounding boxes
img.show()

save = True
if save:
    img.save(f'../updates/images/{image_name}_tesseractOCR.png')

