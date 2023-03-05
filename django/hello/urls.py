from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("/your_name/", ),
    # path("", views.get_name, name="get_name/"),
    path("takePhoto", views.take_photo, name="takePhoto"),
]