import cv2
import time
import numpy as np

# Load image, grayscale, Gaussian blur, Otsu's threshold
cam_port = 0
cam = cv2.VideoCapture(cam_port)
time.sleep(3)
result, image = cam.read()
cv2.imwrite("output.png", image)
capture = cv2.imread("output.png")
image = cv2.GaussianBlur(capture, (5,5), 0)
image = cv2.cvtColor(capture, cv2.COLOR_BGR2HSV)

lower = np.array([0, 0, 0],np.uint8)
upper = np.array([180, 255, 50],np.uint8)
separated = cv2.inRange(image,lower,upper)

# Find bounding box
contours,hierarchy=cv2.findContours(separated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
max_area = 0
largest_contour = None
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        largest_contour=contour
        if largest_contour.all() != None:
            moment = cv2.moments(largest_contour)
            if moment["m00"] > 1000:
                rect = cv2.minAreaRect(largest_contour)
                rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                (width,height)=(rect[1][0],rect[1][1])
                print (str(width)+" "+str(height)+" "+str(width/height))
                box = cv2.boxPoints(rect)
                box = np.intp(box)
                if(height>0.9*width and height<1.1*width):
                    cv2.drawContours(capture,[box], 0, (0, 0, 255), 2)
                else:
                    cv2.drawContours(capture,[box], 0, (255, 0, 0), 2)
                     


cv2.imshow("image", capture)
cv2.waitKey()
