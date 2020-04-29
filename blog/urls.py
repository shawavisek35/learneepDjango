from django.urls import path , include
from . import views

urlpatterns = [
    path("" , views.blogHome , name = "blogHome"),
    path("viewblog/" , views.viewPost , name="viewPost"),
    path("addPost/" , views.addPost , name = "addPost"),
]