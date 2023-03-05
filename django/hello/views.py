from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from json import dumps
import numpy as np
import time
import cv2
import math

from .forms import takePhoto
from .models import userDistance
from .forms import UserDistanceValue

def take_photo(request):
    if request.method == 'POST':
        form = takePhoto(request.POST)      #photo button has been pressed
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        # time.sleep(1)
        result, image = cam.read()
        # filename = './media/testOutput.png'     #saves capture to /django/media folder
        filename = './hello/static/testOutput.png'     #saves capture to /django/hello/static folder
        cv2.imwrite(filename, image)

        #-----------square Scan start-----------
        capture = image
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
                largest_contour = contour
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

        filenameCapture = './hello/static/testCapture.png'     #saves image to /django/hello/static folder
        cv2.imwrite(filenameCapture, capture)
        # cv2.imshow("image", capture)
        # cv2.waitKey()

        #-----------square Scan end -----------
        distForm = UserDistanceValue(request.POST)
        obj = userDistance()
        # obj.distance = (width + height)/2       #saves the distance as an average of the box height & width
        obj.distance = math.sqrt(max_area)
        obj.save()
        print("-------------Saved distance-------------")

        # return render(request, 'hello/visionTest.html')
        return startVisionTest(request)
    else:
        print("-------------Square not found!-------------")
        form = takePhoto(request.POST)
    
    return render(request, 'hello/home.html', {'form': form})

def startVisionTest(request):
    #read saved distance
    finalDistance = max(userDistance.objects.all(), key=id).distance
    # print("Side length:" + str(finalDistance))
    scale = 2
    eyeChartHeight = 698
    eyeChartWidth = 67
    eyeChartHeightScaled = eyeChartHeight * scale
    eyeChartWidthScaled = eyeChartWidth * scale
    context = {
        "user_distance": finalDistance,
        "scaled_height": eyeChartHeightScaled,
        "scaled_width": eyeChartWidthScaled,
        }
    return render(request, 'hello/visionTest.html', context)


def home(request):
    # return render(
    #     request,
    #     # 'hello/landingPage.html',
    #     'hello/home.html',
    # )
    return render(request, 'hello/home.html')

# def pic_button(request):
#     if request.method == "POST":
#         print("button pressed")
#         # return redirect('hello/landingPage.html')
#     else:
#         print("Error taking photo")

# from .forms import NameForm
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return render(request, 'hello/landingPage.html')
#             # return HttpResponseRedirect('/hello/landingPage.html')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'hello/home.html', {'form': form})
