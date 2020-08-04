from django.shortcuts import render , redirect
from django.contrib import messages


from django.contrib.auth.models import User






def home(request):
    return render(request,"home.html")
    

def register(request):     
    return render(request,"register.html")


def login_main(request):
    return render(request,"login.html")

def contact(request):
    pass

def about(request):
    pass





