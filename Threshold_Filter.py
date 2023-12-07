import cv2
import numpy as np


def Threshold(image_path):
    # Load an image
    img= cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    # Set the threshold value 
    threshold_value = 80

    # Apply the threshold filter
    ret, thresholded_image = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

    cv2.imshow('Thresholded Image', thresholded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Threshold('0b9aec984321bf53.jpg')    