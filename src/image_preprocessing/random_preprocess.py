import os
import random
import cv2
import numpy as np
from PIL import Image
import tempfile
import matplotlib.pyplot as plt

# Define path to the directory containing images
images_path = '../../raw_data/images'

# Get a list of all image files in the directory
all_images = [img for img in os.listdir(images_path) if img.endswith('.png') or img.endswith('.jpg')]

# Select a random image
image_name = random.choice(all_images)
img_path = os.path.join(images_path, image_name)

# Load the random image
img = cv2.imread(img_path)

# Function to display the image
def show_image(title, image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# 1. Normalization
def normalize_image(image):
    norm_img = np.zeros((image.shape[0], image.shape[1]))
    normalized_img = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)
    show_image("Normalized Image", normalized_img)
    return normalized_img

# 2. Skew Correction 
def deskew(image):
    co_ords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(co_ords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    show_image("Deskewed Image", rotated)
    return rotated

# 3. Image Scaling
def set_image_dpi(image):
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    length_x, width_y = pil_img.size
    factor = min(2, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = pil_img.resize(size, Image.Resampling.LANCZOS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(1000, 1000))
    scaled_img = cv2.imread(temp_filename)
    show_image("Scaled Image", scaled_img)
    return scaled_img

# 4. Noise Removal
def remove_noise(image):
    denoised_img = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 3)
    show_image("Denoised Image", denoised_img)
    return denoised_img

# 5. Thinning and Skeletonization
def thinning(image):
    kernel = np.ones((5, 5), np.uint8)
    thinned_img = cv2.erode(image, kernel, iterations=1)
    show_image("Thinned Image", thinned_img)
    return thinned_img

# 6. Grayscale Conversion
def get_grayscale(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show_image("Grayscale Image", gray_img)
    return gray_img

# 7. Thresholding (Binarization)
def thresholding(image):
    # _, image = cv2.threshold(image, 0, 255, cv2.THRESH_TOZERO)
    # _,bin_image = cv2.threshold(img,0,50,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # show_image("Binary Image", bin_image)
    
    # Proposed method
    (_, bin_image) = cv2.threshold(image, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    show_image ("Binary Image", bin_image*255)

    return bin_image

def threshtest(image):
    ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret,thresh2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret,thresh3 = cv2.threshold(img,0,255,cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    ret,thresh4 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret,thresh5 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
 
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
     
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
     
    plt.show()

def show_original_image(image):
    show_image("Original Image", image)
    return image

# Apply each preprocessing step 
img = show_original_image(img)
img = normalize_image(img)
img = set_image_dpi(img)
img = show_original_image(img)
img = remove_noise(img)
# img = thinning(img)
img = get_grayscale(img)
# threshtest(img)
img = thresholding(img)
# img = deskew(img)

