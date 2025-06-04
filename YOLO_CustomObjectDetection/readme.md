yolov4

object detector architectures
--------------------------------------------------------------------------------------------------
two stage detector                                                                                |
-------------------------------------------------                                                 |
one stage detector                               |                                                |
input --> backbone --> neck --> dense prediction  |--> sparse prediction                           |
-------------------------------------------------                                                 |
--------------------------------------------------------------------------------------------------

backbone --> CSPDARKNET53

pjreddie.com/darknet/yolo

INSTALLATION:
1. Download & Install Anaconda from website
2. using anaconda prompt: pip install opencv-python
3. test the installation:
    import cv2
    print(cv2.__version__)


CNN: used for image analysis:
    1. scene classification
    2. object detection
    3. segmentation
3 layers of CNN:
    1. convolutional layers
    2. pooling layers
    3. fully-connected layers

IN normal NN: each input neuron is connected to next hidden layer
IN Conv NN: only a small region of input layer neurons connect to neurons hidden layer. These regions in input layer is called as 'Local Receptive Fields'. 'Local receptive fields are scanned/translated across the image to create a feature map.
    Filters: the fixed square called a patch or local receptive field.
    Feature Maps: feature map is output of one filter applied to previous layer

    Activation layer: transformation of the output using activation functional like ReLU
    Pooling: feature map dimensionality is reduced using pooling.

commands to run:
1. create a venv
    python3 -m venv venv
    On macOS/Linux: source venv/bin/activate
    On Windows (Command Prompt): venv\Scripts\activate
2. download yolo files from : https://pjreddie.com/darknet/yolo/
                              YOLOv3-416	COCO trainval	test-dev	55.3	65.86 Bn	35	cfg	weights
