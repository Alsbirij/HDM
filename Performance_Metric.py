import cv2
import numpy as np
import os
import time

# Initialize parameters
__win_name = "Object Detection"
__network = cv2.dnn.readNet("yolov3.cfg", "yolov3.weights")

# Load class labels
with open("coco.names", "r") as file:
    __classes = [line.strip() for line in file.readlines()]

# Initialize font and colors
__font = cv2.FONT_HERSHEY_PLAIN
__colors = np.random.uniform(0, 255, (len(__classes), 3))

# Specify the path of images
images_path = r"C:\Users\Alsbirij\Desktop\alsbirij\dataset\images"

# List of images to process
image_files = [os.path.join(images_path, f) for f in os.listdir(images_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Specify the path where you want to save the files
output_path = r"C:\Users\Alsbirij\Desktop\alsbirij\dataset\predicted_Labels"

# Ensure that the output directory exists
os.makedirs(output_path, exist_ok=True)

# Start the timer
start_time = time.time()

# Process each image
for image_file in image_files:
    # Load the image
    __img = cv2.imread(image_file)
    img_h, img_w, img_c = __img.shape

    # Get network layers
    layer_names = __network.getLayerNames()
    output_layers = [layer_names[i - 1] for i in __network.getUnconnectedOutLayers()]

    # Process the image
    blob = cv2.dnn.blobFromImage(__img, scalefactor=0.00392, size=(416, 416), mean=(0, 0, 0), swapRB=True, crop=False)
    __network.setInput(blob)
    outputs = __network.forward(output_layers)

    # Initialize lists for detection data
    bounding_boxes = []
    classes_id = []
    confidences = []

    # Process each detection
    for out in outputs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if class_id == 0 and confidence > 0.5:  # Filter by 'person' class and confidence
                center_x = int(detection[0] * img_w)
                center_y = int(detection[1] * img_h)
                w = int(detection[2] * img_w)
                h = int(detection[3] * img_h)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                bounding_boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                classes_id.append(class_id)

    # Non-max suppression
    indices = cv2.dnn.NMSBoxes(bounding_boxes, confidences, 0.4, 0.4)

    # Write detected labels in YOLO format
    label_file_name = f"{os.path.basename(image_file).split('.')[0]}.txt"
    full_path = os.path.join(output_path, label_file_name)
    with open(full_path, "w") as file:
        for i in range(len(bounding_boxes)):
            if i in indices:
                x, y, w, h = bounding_boxes[i]
                # Normalize the coordinates for YOLO format
                center_x = (x + w / 2) / img_w
                center_y = (y + h / 2) / img_h
                norm_w = w / img_w
                norm_h = h / img_h

                # Write in YOLO format
                file.write(f"{classes_id[i]} {center_x} {center_y} {norm_w} {norm_h}\n")

# End the timer
end_time = time.time()

# Calculate total and average time
total_time = end_time - start_time
average_time = total_time / len(image_files) if image_files else 0

# Print the timing information
print(f"All images have been processed in {total_time:.2f} seconds.")
print(f"Average processing time per image: {average_time:.2f} seconds.")
