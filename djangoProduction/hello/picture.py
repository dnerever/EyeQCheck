import cv2  #pip install opencv-contrib-python
import numpy as np
import time

cam_port = 0
cam = cv2.VideoCapture(cam_port)
time.sleep(3)
result, image = cam.read()



if result:
    # cv2.imshow("testImage", image)
    cv2.imwrite("django/hello/static/output.png", image)
    cv2.waitKey(0)
    cv2.destroyWindow("testImage")
else:
    print("No image. Try again")
