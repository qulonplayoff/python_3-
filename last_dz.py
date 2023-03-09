import cv2

net = cv2.dnn.readNetFromDarknet('yolov4.cfg', 'yolov4.weights')

classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

colors = np.random.uniform(0, 255, size=(len(classes), 3))

image = cv2.imread('test_image.jpg')

height, width, _ = image.shape

blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

net.setInput(blob)

output_layers = net.getUnconnectedOutLayersNames()
outputs = net.forward(output_layers)

class_ids = []
confidences = []
boxes = []

for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x,
