import os
import random
import easyocr
from PIL import Image, ImageDraw
from paddleocr import PaddleOCR, draw_ocr



# Define path to the directory containing images
images_path = '../raw_data/images'

# Get a list of all image files in the directory
all_images = [img for img in os.listdir(images_path) if img.endswith('.png') or img.endswith('.jpg')]

# Select a random image
image_name = random.choice(all_images)
img_path = os.path.join(images_path, image_name)

# Load the random image
img = Image.open(img_path)

results = easyocr.Reader(['en']).readtext(img_path)
# results: [([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], 'text', prob),...]

image = Image.open(img_path).convert('RGB')

# Extract boxes and words
boxes = [line[0] for line in results]
words = [line[1] for line in results]

# Draw bounding boxes
font_path = '/Library/Fonts/Arial.ttf'
draw_img = draw_ocr(image, boxes, words, font_path=font_path)
draw_img_pil = Image.fromarray(draw_img)
draw_img_pil.show()

# save this image to ../updates/images for weekly update
save = True
if save:
    draw_img_pil.save(f'../updates/images/{image_name}_easyOCR.png')

