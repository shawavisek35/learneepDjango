from django.shortcuts import render , redirect
from pymongo import MongoClient



#connecting with mongo atlas
client = MongoClient("mongodb+srv://Avisek:Avisek3524@a4-iszf9.azure.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database("learneep")
blog = db.blogs

# Create your views here.

def blogHome(request):
    return render(request,"blog/home.html")

def viewPost(request):
    pass

def addPost(request):
    if request.method=="POST":
        heading = request.POST['heading']
        para = request.POST["editor"]
        print("para = ", para)
        return render(request , "blog/addPost.html" , {'post' : para})
    return render(request,"blog/addPost.html")
