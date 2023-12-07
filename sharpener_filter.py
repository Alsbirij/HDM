import cv2
import numpy as np

def sharpen_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Check if image is loaded
    if img is None:
        print("Error: Image not found or the path is incorrect")
        return

    # Get the height, width, and channels of the image (if needed)
    #height, width, channels = img.shape

    # Define the sharpening filter
    sharpening_filter = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    # Apply the filter to sharpen the image
    sharpened_image = cv2.filter2D(img, -1, sharpening_filter)

    # Display the sharpened image in a separate window
    cv2.imshow('Sharpened Image', sharpened_image)

    # Wait for a key press to close the windows
    cv2.waitKey(0)

    # Close all open windows
    cv2.destroyAllWindows()

# Call the function with the image path
sharpen_image('0b9aec984321bf53.jpg')
