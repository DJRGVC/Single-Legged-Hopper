import os
import random
import easyocr
from PIL import Image, ImageDraw
from paddleocr import PaddleOCR, draw_ocr
import pandas as pd

gtruth_csv_path = '../raw_data/labels.csv'

def get_ground_truth_text(img_path):
    # load in csv with pandas
    df = pd.read_csv(gtruth_csv_path)
    # find row with image path
    row = df.loc[df['image_path'] == img_path]
    # get the ground truth text
    ground_truth_text = row['text']
    return ground_truth_text

# Define path to the directory containing images
images_path = '../raw_data/images'

# find number of files in images_path
all_images = os.listdir(images_path)

# choose random number between 0 and number of files in images_path
number = random.randint(0, len(all_images))

# now, choose file to be:
img_path = images_path + f'/slide_{number}_image_1.png'
print(img_path)

# now, from ../raw_data/labels.csv, get the ground truth text for this image using image path
ground_truth_text = get_ground_truth_text(img_path)
# print the text 
print(ground_truth_text)

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
save = False
if save:
    draw_img_pil.save(f'../updates/images/{image_name}_easyOCR.png')


