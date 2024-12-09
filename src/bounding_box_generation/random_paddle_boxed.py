import os
import csv
import random
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
from Levenshtein import distance as levenshtein_distance

# Initialize PaddleOCR with English language model
ocr = PaddleOCR(use_angle_cls=True, lang='en')
font_path = '/Library/Fonts/Arial.ttf'  # Ensure this font path is valid on your system

# Define paths
images_path = '../raw_data/images'
transcriptions_file = '../raw_data/labels.csv'

# Load transcriptions from CSV into a dictionary {image_name: transcription}
transcriptions = {}
with open(transcriptions_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        image_name, transcription = row
        transcriptions[image_name] = transcription.split()  # Split transcription into words

# Function to match OCR words with transcription words using Levenshtein distance
def match_words(ocr_words, transcribed_words):
    matched_words = []
    for ocr_word in ocr_words:
        closest_word = min(transcribed_words, key=lambda w: levenshtein_distance(ocr_word, w))
        matched_words.append(closest_word)
        transcribed_words.remove(closest_word)  # Remove matched word to avoid re-use
    return matched_words


# Iterate over images in the images directory, perform OCR, and match already transcribed words (using Levenshtein distance)
# Only do so over n random images (for testing purposes). If n=-1, iterate over all images.
def process_images(n=3):
    # Get list of all image files
    all_images = [img for img in os.listdir(images_path) if img.endswith('.png')]

    # Limit to n random images if n is specified and greater than zero
    if n > 0:
        images_to_process = random.sample(all_images, n)
    else:
        images_to_process = all_images

    # Process each selected image
    for image_name in images_to_process:
        img_path = os.path.join(images_path, image_name)

        # Perform OCR on the image
        result = ocr.ocr(img_path, cls=True)

        # Extract bounding boxes and OCR-detected words
        boxes = [line[0] for line in result[0]]
        ocr_words = [line[1][0] for line in result[0]]

        # Get the corresponding transcription for this image
        transcribed_words = transcriptions.get(image_name, [])

        # Match OCR words with transcription words
        if transcribed_words:
            matched_words = match_words(ocr_words, transcribed_words)
        else:
            matched_words = ocr_words  # If no transcription, use OCR words as-is

        # Load the image
        image = Image.open(img_path).convert('RGB')

        # Draw bounding boxes with matched transcriptions
        draw_img = draw_ocr(image, boxes, matched_words, font_path=font_path)
        draw_img_pil = Image.fromarray(draw_img)

        save = True
        if save:
            draw_img_pil.save(f'../updates/images/{image_name}_paddleOCR.png')

        
        # Display the image with bounding boxes
        draw_img_pil.show()

# Set n to the desired number of images to process; set to -1 to process all images
process_images(n=3)
