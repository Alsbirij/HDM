import cv2
import numpy as np


def BrightneesCorrection(image_path):
    # Load an image
    image = cv2.imread(image_path)


    # Define the brightness factor (adjust as needed)
    brightness_factor = 1.5  # Increase to make it brighter, decrease to make it darker

    # Apply brightness correction
    brightened_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

    cv2.imshow('Corrected Image', brightened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
#BrightneesCorrection('0b9aec984321bf53.jpg')    
