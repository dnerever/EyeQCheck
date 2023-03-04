from cv2 import *  #pip install opencv-contrib-python
import numpy as np

cam_port = 0
cam = VideoCapture(cam_port)

result, image = cam.read()

if results:
    imshow("testImage", image)
    imwrite("testImage.png", image)
    waitKey(0)
    destroyWindow("testImage")

else:
    print("No image. Try again")
