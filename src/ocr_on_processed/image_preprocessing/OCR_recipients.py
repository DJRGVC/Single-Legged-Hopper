import os
import random
import cv2
import numpy as np
from PIL import Image, ImageDraw
import tempfile
import matplotlib.pyplot as plt

# import SkewCorrection module to use static method correct_skew() from file skew_correction.py
from skew_correction import SkewCorrection

# Define path to the directory containing images
images_path = '../../raw_data/images'

# define path to save the processed images
processed_images_path = '../../raw_data/processed_images'

# Get a list of all image files in the directory
all_images = [img for img in os.listdir(images_path) if img.endswith('.png') or img.endswith('.jpg')]

# Select a random image
image_name = random.choice(all_images)
img_path = os.path.join(images_path, image_name)
image_name = image_name.split('.')[0]

# Load the random image
img = cv2.imread(img_path)

def process_image(img, threshhold_offset, gaussian_blur=False, save_skew=False):
    # Rescale the image, if needed.
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    orig_img = img.copy()

    print("processing")

    # Converting to gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("converted to gray")

    # Removing Shadows
    rgb_planes = cv2.split(img)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
    img = cv2.merge(result_planes)

    print("removed shadows")

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)

    print("applying dilation and erosion")

    # increases the white region in the image 
    img = cv2.dilate(img, kernel, iterations=1)

    print("dilated")

    # erodes away the boundaries of foreground object
    img = cv2.erode(img, kernel, iterations=1) 

    print("eroded")

    # Apply blur to smooth out the edges
    if gaussian_blur:
        img = cv2.GaussianBlur(img, (5, 5), 0)
        print("blurred")

    # Calculate Otsu's threshold and subtract an offset
    otsu_threshold, _ = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    adjusted_threshold = max(otsu_threshold + threshhold_offset, 0) 
    _, img = cv2.threshold(img, adjusted_threshold, 255, cv2.THRESH_BINARY)

    print("thresholded")

    # correct skew (UNCOMMENT THIS WHEN NOT TESTING THRESHHOLDS)
    original_img = img
    angle, img = SkewCorrection.nathan_skew_correction(img, orig_img)
    print(f"Angle of rotation: {angle}")
    show_image("Unskewed Image", img)

    print("skew corrected")

    # Save the skew corrected image
    if save_skew:
        # save the skew corrected image as jpg in processed image path
        cv2.imwrite(f'{processed_images_path}/skew_corrected_{image_name}', img)
        # save the original image
        cv2.imwrite(f'{processed_images_path}/original_{image_name}', original_img)

        print("saved skew corrected image")

    return img

# Function to display the image
def show_image(title, image, save=False):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def show_original_image(image, save=False):
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    plt.show()
    if save:
        plt.savefig(f'{processed_images_path}/original_{image_name}.png')
    return image

def show_multiple_offsets(img, offsets, gaussian_blur=False, save=False):
    # Display 3x3 grid of images
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    if gaussian_blur:
        fig.suptitle("Processed Images with Different Threshold Offsets and Gaussian Blur", fontsize=16)
    else:
        fig.suptitle("Processed Images with Different Threshold Offsets", fontsize=16)

    # Iterate over the offsets and plot each processed image
    for i, offset in enumerate(offsets):
        # Process the image with the current offset
        processed_img = process_image(img, offset, gaussian_blur)
        
        # Determine row and column in the 2x2 grid
        row, col = divmod(i, 2)
        ax = axes[row, col]
        ax.imshow(processed_img, cmap='gray')
        ax.set_title(f"Offset: {offset}")
        ax.axis('off')

    # Hide any unused subplots 
    for j in range(i + 1, 4):
        row, col = divmod(j, 2)
        axes[row, col].axis('off')

    # Adjust space between images
    plt.subplots_adjust(hspace=0.05, wspace=0.05)

    # convert offsets to string
    offset = str(offsets[0])

    # remove .png from image name
    if save:
        if gaussian_blur:
            plt.savefig(f'{processed_images_path}/processed_{image_name}_{offset}_gaussian.png')
        else:
            plt.savefig(f'{processed_images_path}/processed_{image_name}_{offset}.png')

    plt.show()

# img = process_image(img)
# show_image("Processed Image", img)

# img = process_image(img, 15, False, False)

# function to take a single image, process it, rotate it, display it, and optionally save it as a jpg to the processed images path.
def show_single_rotated_and_processed_image(img, offset=15, gaussian_blur=False, save=False):
    # Process the image
    print("uno")
    processed_img = process_image(img, offset, gaussian_blur, False)
    print("dos")
    # Display the processed image
    show_image("Processed Image", processed_img)

    print("tres")

    # Save the processed image
    if save:
        # convert the processed image to a PIL image
        draw_img_pil = Image.fromarray(processed_img)

        # save the processed image
        draw_img_pil.save(f'{processed_images_path}/processed_{image_name}.jpg')

        print("saved processed image")

show_single_rotated_and_processed_image(img, 15, False, True)





# TO GENERATE IMAGES FOR REPORT COMPARING OFFSETS AND GAUSSIAN BLUR
# offsets = [40, 20, 0, -20]
# show_multiple_offsets(img, offsets, False, True)
# show_multiple_offsets(img, offsets, True, True)
# 
# offsets = [30, 25, 20, 15]
# show_multiple_offsets(img, offsets, False, True)
# show_multiple_offsets(img, offsets, True, True)
# 
# # also save original, unprocessed image
# show_original_image(img, True)


