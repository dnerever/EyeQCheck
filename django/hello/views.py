from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import time

import cv2  #pip install opencv-contrib-python
import numpy as np


# Create your views here.
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

from .forms import NameForm

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

from .forms import takePhoto

def take_photo(request):
    if request.method == 'POST':
        form = takePhoto(request.POST)      #photo button has been pressed
        # time.sleep(5)

        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        time.sleep(1)
        result, image = cam.read()

        if result:
            # cv2.imshow("testImage", image)
            cv2.imwrite("static/output2.png", image)
            # cv2.waitKey(0)
            # cv2.destroyWindow("testImage")
            print("taking photo")
        else:
            print("No image. Try again")

        return render(request, 'hello/home.html')
    else:
        form = takePhoto(request.POST)
    
    return render(request, 'hello/home.html', {'form': form})
