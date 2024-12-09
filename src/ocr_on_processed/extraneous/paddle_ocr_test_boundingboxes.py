from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

# Initialize PaddleOCR with English or specific language model
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Load and process the image
img_path = 'slide_256_image_1.png'

result = ocr.ocr(img_path, cls=True)

# Open the image
image = Image.open(img_path).convert('RGB')

# Extract boxes and words
boxes = [line[0] for line in result[0]]
words = [line[1][0] for line in result[0]]

# Draw bounding boxes
font_path = '/Library/Fonts/Arial.ttf'
draw_img = draw_ocr(image, boxes, words, font_path=font_path)
draw_img_pil = Image.fromarray(draw_img)
draw_img_pil.show()

# save this image to ../updates/images for weekly update
save = True
if save:
    draw_img_pil.save(f'../updates/images/{image_name}_paddleOCR.png')

