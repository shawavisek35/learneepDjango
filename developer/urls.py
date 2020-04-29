from django.urls import path , include
from . import views

urlpatterns = [
    path("" , views.developerHome , name = "developerHome"),
]