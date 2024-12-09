print("os")
import os
print("random")
import random
print("easyOCR")
import easyocr
print("PIL")
from PIL import Image, ImageDraw
print("paddleocr")
from paddleocr import draw_ocr


print("imports completed")

print("defining path to images")

# Define path to the directory containing images
images_path = '../../raw_data/images'


print("loading images")

# Get a list of all image files in the directory
all_images = [img for img in os.listdir(images_path) if img.endswith('.png') or img.endswith('.jpg')]

print("select random image")

# Select a random image
image_name = random.choice(all_images)
img_path = os.path.join(images_path, image_name)

print("loading image")

# Load the random image
img = Image.open(img_path)

print("running easyOCR")

results = easyocr.Reader(['en']).readtext(img_path)
# results: [([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], 'text', prob),...]

print("convert to RGB")

image = Image.open(img_path).convert('RGB')

print("extracting boxes and words")

# Extract boxes and words
boxes = [line[0] for line in results]
words = [line[1] for line in results]

print("drawing boxes")

# Draw bounding boxes
font_path = '/Library/Fonts/Arial.ttf'
draw_img = draw_ocr(image, boxes, words, font_path=font_path)
draw_img_pil = Image.fromarray(draw_img)

print("showing image")

draw_img_pil.show()

print("saving image")

# save this image to ../updates/images for weekly update
save = False

if save:
    draw_img_pil.save(f'../../../updates/images/{image_name}_easyOCR.png')
