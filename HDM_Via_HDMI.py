import cv2
import numpy as np

def Webcam_Detection_Function():
    # Load the YOLO model
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

    # Read the class names from the COCO file
    classes = []
    with open('coco.names', 'r') as f:
        classes = f.read().strip().splitlines()

    # Use the first webcam as the video source
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    # Open a window on a secondary monitor
    window_name = 'Webcam Image'
    window_x, window_y = 0, 1920  # Adjust these for your monitor setup
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, window_x, window_y)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # Read a frame from the webcam
        ret, img = cap.read()

        # Break the loop if there's no more frames
        if not ret:
            break

        # Get the height, width, and number of channels of the frame
        height, width, channels = img.shape

        # Create a blob from the image
        blob = cv2.dnn.blobFromImage(img, scalefactor=1/255, size=(416, 416), mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)

        # Get the names of the output layers
        output_layers_names = net.getUnconnectedOutLayersNames()

        # Forward pass to obtain predictions
        layerOutputs = net.forward(output_layers_names)

        boxes = []
        confidences = []
        class_ids = []

        # Iterate through each detection
        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Filter out detections that are not people
                if class_id == classes.index("person") and confidence > 0.5:
                    # Get coordinates for drawing the bounding box
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Perform non-max suppression
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(boxes), 3))

        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence = str(round(confidences[i], 2))
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 255, 255), 2)

        # Show the image in the window
        cv2.imshow(window_name, img)

        key = cv2.waitKey(1)
        if key == 27:  # ASCII for ESC key
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

Webcam_Detection_Function()
