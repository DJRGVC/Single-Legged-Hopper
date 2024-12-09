import os
import sys

MODULES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src'))
sys.path.append(MODULES_DIR)

from modules.easy_ocr_processor import EasyOCRProcessor
from modules.image_preprocessor import ImagePreprocessor
from modules.skew_correction import SkewCorrection

def process_and_ocr():

    print("Processing and OCRing a random image...")

    # Define paths
    images_path = "../../raw_data/images"
    processed_images_path = "../../raw_data/processed_images"
    save_path = "../../../updates/images"
    font_path = "/Library/Fonts/Arial.ttf"  # Adjust to the correct path for your system

    # Variables
    threshhold = 18
    blur = True

    print(f"Images path: {images_path}")

    # Initialize the image preprocessor
    image_preprocessor = ImagePreprocessor(images_path, processed_images_path)

    print("Loading a random image and preprocessing it...")

        # return image_name, Image.open(img_path).convert('RGB')

    # Load a random image and preprocess it
    image_name, img = image_preprocessor.load_random_image()
    processed_img, angle = image_preprocessor.process_image(img, threshold_offset=threshhold, gaussian_blur=blur, save_skew=False, image_name=image_name)

    # Show the preprocessed image
    print("Showing Image...")
    image_preprocessor.show_image("Pre-processed Image", processed_img)

    print("Initializing EasyOCR processor...")

    # Initialize the EasyOCR processor
    ocr_processor = EasyOCRProcessor(images_path, save_path, font_path)

    print("Saving the preprocessed image...")

    # Save or show the processed image
    image_preprocessor.save_image(processed_img, f"{image_name}_processed.jpg")

    print("Performing OCR with EasyOCR...")

    # Use EasyOCR on the processed image
    processed_img_path = os.path.join(processed_images_path, f"{image_name}_processed.jpg")

    easyocr_results = ocr_processor.perform_easyocr(processed_img_path)

    print("Convert preprocessed image to PIL image...")
    processed_img = image_preprocessor.convert_to_pil_image(processed_img)

    print("Drawing bounding boxes on the processed image...")
    
    # Draw bounding boxes on the processed image
    ocr_processor.draw_results(processed_img, easyocr_results, show=True, save=True, output_name=f"{image_name}_easyOCR")

if __name__ == "__main__":
    process_and_ocr()
