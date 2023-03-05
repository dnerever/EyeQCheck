import cv2
import time
import numpy as np
import math

# Load image, grayscale, Gaussian blur
time.sleep(3)
cam_port = 0
cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

frame_width = 1280
frame_height = 720
cam.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

result, image = cam.read()
cv2.imwrite("output.png", image)
capture = cv2.imread("output.png")

image = cv2.GaussianBlur(capture, (5,5), 0)
image = cv2.cvtColor(capture, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 0],np.uint8)
upper = np.array([180, 255, 50],np.uint8)
separated = cv2.inRange(image,lower,upper)

# Find bounding box
pixel_width = 0
user_distance = 0
contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
max_area = 0
largest_contour = None
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        largest_contour=contour
        pixel_width = math.sqrt(max_area)
        if largest_contour.all() != None:
            moment = cv2.moments(largest_contour)
            if moment["m00"] > 1000:
                rect = cv2.minAreaRect(largest_contour)
                rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                (width,height)=(rect[1][0],rect[1][1])
                # print (str(width)+" "+str(height)+" "+str(width/height))
                box = cv2.boxPoints(rect)
                box = np.intp(box)
                # Draw desired square in image
                if(height>0.9*width and height<1.1*width):
                    cv2.drawContours(capture,[box], 0, (0, 0, 255), 2)
                    user_distance = 24*92/pixel_width
                #Draw other contours found in image
                else:
                    cv2.drawContours(capture,[box], 0, (255, 0, 0), 2)
                     



if user_distance != 0:
    print("User Distance: "+ str(user_distance)+ " inches")
    eye_chart = cv2.imread("eyechart.png")
    h, w = eye_chart.shape[:2]
    print(str(h)+" "+str(w))
    new_h, new_w = int((2/3)*h*(user_distance/12)), int((2/3)*w*(user_distance/12)) 
    resizeImg = cv2.resize(eye_chart, (new_w, new_h))
    cv2.imshow("resiezed", resizeImg)
else:
    print("Cannot find squares, please retake picture!")
cv2.imshow("capture", capture)

cv2.waitKey()
