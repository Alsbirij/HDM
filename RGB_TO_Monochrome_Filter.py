import cv2

def display_grayscale(image_path):
    # Load an RGB image
    img = cv2.imread(image_path)

    # Get the height, width, and channels of the image
    height, width, channels = img.shape



    # Convert the RGB image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Grayscale Image', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the image path
display_grayscale('0b9aec984321bf53.jpg')
