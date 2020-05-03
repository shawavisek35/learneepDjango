from django.shortcuts import render , redirect
from pymongo import MongoClient
import datetime
from .models import BlogPost



#connecting with mongo atlas
client = MongoClient("mongodb+srv://Avisek:Avisek3524@a4-iszf9.azure.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database("learneep")
blogs = db.blogs

# Create your views here.

def blogHome(request):
    return render(request,"blog/home.html")

def viewPost(request):
    pass

def addPost(request):
    if request.method=="POST":
        title = request.POST['heading']
        category = request.POST["category"]
        tags = request.POST["tags"]
        article = request.POST["editor"]
        thumbnail = request.FILES['thumbnail']
        username = request.user.username
        published_date = datetime.datetime.now()
        image = datetime.datetime.timestamp(published_date)
        print(thumbnail , published_date , image)

        newBlog = {
            'user_name' : username,
            'title' : title,
            'category' : category,
            'tags' : tags,
            'article' : article,
            'image' : image,
            'published_date' : published_date
        }

        #blogs.insert_one(newBlog)
        return redirect("addPost")
        
        
    return render(request,"blog/addPost.html")
