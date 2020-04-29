from django.shortcuts import render

# Create your views here.

def teacherHome(request):
    return render(request,"teacher/home.html")
