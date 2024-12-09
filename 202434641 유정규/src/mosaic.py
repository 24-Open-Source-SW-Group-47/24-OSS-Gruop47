import cv2
import numpy as np
import os

# Set paths for YOLO model files
yolo_weights = "./yolov3.weights"  # YOLO weights file
yolo_config = "./yolov3.cfg"       # YOLO configuration file
coco_names = "./coco.names"        # Class names file

# Get image path from user input
image_path = input("Enter the image path (e.g., 'sample.jpg' if in the current folder, absolute/relative paths are also allowed): ").strip()

# Get the target object name from user input
target_object = input("Enter the name of the object to apply mosaic (e.g., person, car, dog): ").strip()

# Get mosaic strength from user input (1 ~ 100)
while True:
    try:
        mosaic_strength = int(input("Enter the mosaic strength (integer between 1 and 100): ").strip())
        if 1 <= mosaic_strength <= 100:
            break
        else:
            print("Please enter an integer between 1 and 100.")
    except ValueError:
        print("Please enter a valid integer.")

# Load class names
with open(coco_names, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Check if the entered object exists in the COCO dataset
if target_object not in classes:
    print(f"'{target_object}' is not included in the COCO dataset.")
    exit()

# Set up YOLO network
net = cv2.dnn.readNet(yolo_weights, yolo_config)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

# Read the image
if not os.path.exists(image_path):
    print("The image does not exist at the specified path.")
    exit()

image = cv2.imread(image_path)
if image is None:
    print("Failed to load the image.")
    exit()

height, width, channels = image.shape

# Preprocess the image for YOLO
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
outputs = net.forward(output_layers)

# Process YOLO output
boxes = []
confidences = []
class_ids = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:  # Confidence threshold
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply Non-Maximum Suppression (NMS) to remove duplicates
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Apply mosaic effect
found = False
for i in indexes.flatten():
    label = str(classes[class_ids[i]])
    if label == target_object:  # Compare with the user-specified object
        x, y, w, h = boxes[i]
        mosaic_part = image[y:y+h, x:x+w]

        # Determine the downscale ratio based on mosaic strength
        small_w = max(1, w // mosaic_strength)
        small_h = max(1, h // mosaic_strength)

        small = cv2.resize(mosaic_part, (small_w, small_h), interpolation=cv2.INTER_LINEAR)
        mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = mosaic
        found = True
        print(f"'{target_object}' has been mosaicked. (Strength: {mosaic_strength})")

if not found:
    print("The specified object was not detected in the image.")

# Resize the image for better visualization
display_width = 800  # Display width for visualization
scale_ratio = display_width / width
resized_image = cv2.resize(image, (display_width, int(height * scale_ratio)))

# Display the result
cv2.imshow("Result", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
