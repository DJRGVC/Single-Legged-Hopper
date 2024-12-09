import cv2
import numpy as np
from scipy.ndimage import interpolation as inter
import pytesseract

# Class to correct skewness in the image (imported as a module in OCR...py)
class SkewCorrection:
    # Method adapted from: nathancy
    # https://stackoverflow.com/questions/57964634/python-opencv-skew-correction-for-ocr
    @staticmethod
    def nathan_skew_correction(image, ex=None, delta=1, limit=30):
        def determine_score(arr, angle):
            data = inter.rotate(arr, angle, reshape=False, order=0)
            histogram = np.sum(data, axis=1, dtype=float)
            score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
            return histogram, score

        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
        thresh = image

        scores = []
        angles = np.arange(-limit, limit + delta, delta)
        # exclude 0 since it's the original image
        angles = angles[angles != 0]

        for angle in angles:
            histogram, score = determine_score(thresh, angle)
            scores.append(score)

        best_angle = angles[scores.index(max(scores))]

        # if score for 0 is twice as high as the next best angle, then don't rotate
        if max(scores) > 2 * sorted(scores)[-2]:
            best_angle = 0

        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
        corrected = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
                borderMode=cv2.BORDER_REPLICATE)

        return best_angle, corrected

    # Method adapted from: Sreekiran A R
    # https://stackoverflow.com/questions/62670920/90-degree-skew-correction-for-ocr-in-opencv-python
    @staticmethod
    def sree_skew_correction(image, ex=None):

        def rotate_bound(image, angle):
            """Rotate image with the given angle

            :param type image: input image
            :param type angle: Angle to be rotated
            :return: rotated image
            :rtype: numpy.ndarray

            """
            (h, w) = image.shape[:2]
            ### centroid
            (cX, cY) = (w // 2, h // 2)
            ### creating rotation matrix
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)

            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY

            return cv2.warpAffine(image, M, (nW, nH))

        # getting orientation info
        newdata=pytesseract.image_to_osd(image)

        # filter angle value
        angle=re.search('(?<=Rotate: )\d+', newdata).group(0)

        # rotating image with angle
        skew_corrected_image=rotate_bound(image,float(angle))

        return 0, skew_corrected_image

    # Method adapted from: Netra Prasad Neupane
    # https://netraneupane.medium.com/text-skewness-correction-a51fd3a27157
    @staticmethod
    def netra_skew_correction(thresh, image):
        coords = np.column_stack(np.where(thresh > 0)) # (x,y) coordinates of pixels > 0
        angle = cv2.minAreaRect(coords)[-1] # angle of minimum rotated bounding box
        if angle < -45:
            angle = -(90 + angle)
        # otherwise, just take the inverse of the angle to make
        else:
            angle = -angle

        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0) # get rotation matrix
        rotated_image = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        return angle, rotated_image

