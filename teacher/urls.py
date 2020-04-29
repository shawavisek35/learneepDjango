from django.urls import path , include
from . import views

urlpatterns = [
    path("" , views.teacherHome , name = "teacherHome"),
]