import cv2
import numpy as np

def MedianFilter(image_path):
    # Load an image
    image = cv2.imread(image_path)



    # Apply median filter for noise reduction
    median_filtered = cv2.medianBlur(image, 5)  

    
    
    cv2.imshow('Median Filtered Image', median_filtered)
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#MedianFilter('0b9aec984321bf53.jpg')  
