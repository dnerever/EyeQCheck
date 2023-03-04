import cv2  #pip install opencv-contrib-python
import numpy as np

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    cv2.imshow("testImage", image)
    cv2.imwrite("testImage.png", image)
    cv2.waitKey(0)
    cv2.destroyWindow("testImage")

else:
    print("No image. Try again")
