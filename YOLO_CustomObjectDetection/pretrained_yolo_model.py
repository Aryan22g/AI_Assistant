import numpy as np
import cv2

CONFIG_PATH = 'dataset/yolov3.cfg'
WEIGHTS_PATH = 'dataset/yolov3.weights'
#load the image to detect, get width, height

img_to_detect = cv2.imread('images/testing/scene2.jpg')
img_height = img_to_detect.shape[0]
img_width = img_to_detect.shape[1]

# convert to blob to pass into a model
img_blob = cv2.dnn.blobFromImage(img_to_detect, 1/255.0, (416, 416), swapRB=True, crop=False)

# set of 80 class labels
class_labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat","trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball","kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket","bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair","couch","pottedplant","bed","diningtable","toilet","tv","laptop","mouse","remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]

#declare list of colors as an array
#green, blue, red, cyan, yellow, purple
#split based on ',' and for every split, change type to int
#convert that to a numpy array to apply color mask to the image numpy array
class_colors = ["0,255,0","0,0,255","255,0,0","255,255,0","0,255,255"]
class_colors = [np.array(every_color.split(",")).astype("int") for every_color in class_colors]
class_colors = np.array(class_colors)
class_colors = np.tile(class_colors,(16,1))

# Loading pretrained model
yolo_model = cv2.dnn.readNetFromDarknet(CONFIG_PATH, WEIGHTS_PATH)

#get all the layers from yolo network
yolo_layers = yolo_model.getLayerNames()
yolo_output_layer = [yolo_layers[yolo_layer[0]-1] for yolo_layer in yolo_model.getUnconnectedOutLayers()]

#input preprocessed blob into model and pass through the model
yolo_model.setInput(img_blob)

# obtain the detection layers by forwarding through till the output layer
obj_detection_layers = yolo_model.forward(yolo_output_layer)

#loop over eaach of the layer outputs
for object_detection_layer in obj_detection_layers:
    #loop over the detections
    for object_detection in object_detection_layer:
        # object_detection[1 to 4] ==> will have two center points, box width and box height
        # object_detection[5] ==> will have scores for all objects within the bounding box
        all_scores = object_detection[5:]
        predicted_class_id = np.argmax(all_scores)
        prediction_confidence = all_scores[predicted_class_id]
        #take only predictions with confidence more than 20
        if prediction_confidence > 0.20:
            # get the predicted label
            predicted_class_label = class_labels[predicted_class_id]
            # obtain the bounding box to coordinates for actual image from resized image size
            bounding_box = object_detection[0:4] * np.array([img_width,img_height,img_width,img_height])
            (box_center_x_pt, box_center_y_pt, box_width, box_height) = bounding_box.astype("int")
            start_x_pt = int(box_center_x_pt - (box_width/2))
            start_y_pt = int(box_center_y_pt - (box_height/2))
            end_x_pt = start_x_pt + box_width
            end_y_pt = start_y_pt + box_height
            
            #get a random mask color form the numpy array of colors
            box_color = class_colors[predicted_class_id]
            #convert color numpy array as list and apply text and box
            box_color = [int(c) for c in box_color]
            
            #print the prediciton in console
            predicted_class_label = "{}:{:.2f}%".format(predicted_class_label, prediction_confidence*100)
            print("predicted object {}".format(predicted_class_label))
            
            #draw rectange and text in the image
            cv2.rectangle(img_to_detect, (start_x_pt,start_y_pt),(end_x_pt,end_y_pt),box_color,1)
            cv2.putText(img_to_detect,predicted_class_label,(start_x_pt,start_y_pt-5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)
cv2.imshow("Detection Output", img_to_detect)
