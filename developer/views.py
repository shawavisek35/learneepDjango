from django.shortcuts import render , redirect

# Create your views here.

def developerHome(request):
    return render(request,"developer/home.html")
