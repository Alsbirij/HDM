import cv2

def apply_dummy_filter(image_path):
    img = cv2.imread(image_path)

    def DummyFilter(input_image):
        return input_image

    display_width = 800  # Adjust as needed
    display_height = 600  # Adjust as needed

    # Resize the image for display
    resized_image = cv2.resize(img, (display_width, display_height))
    filtered_image = DummyFilter(resized_image)

    #cv2.imshow('Original Image', resized_image)
    cv2.imshow('Filtered Image', filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the image path
apply_dummy_filter('0b9aec984321bf53.jpg')   