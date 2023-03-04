from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(
        request,
        'hello/landingPage.html',
    )
# def home(request):
#     return HttpResponse("Hello, DJacob")