# This project is to detect the object and if there is any
# sign of fire it will alert us.
# This poject requires 
#

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

# this is to open camera
video = cv2.VideoCapture(0)

# add detected object in the label
labels = []

while True:
    # put video frame to variable
    ret, frame = video.read()
    # to detect the object and make it with box and label
    bbox, label, conf = cv.detect_common_objects(frame)
    # output the video box
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow('Object Detection', output_image)

    for item in label:
        if item in labels:
            # if there are multiple object of same kind it doen't add to the list
            pass
        else:
            labels.append(item)

    # to quit the video box with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# print(labels)