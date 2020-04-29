from django.shortcuts import render , redirect
from django.contrib import messages
import pyrebase
from django.contrib import auth

from django.contrib.auth.models import User
from pymongo import MongoClient

#connecting with mongo atlas
client = MongoClient("mongodb+srv://Avisek:Avisek3524@a4-iszf9.azure.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database("learneep")
users = db.users

user_logged = {}



def home(request):
    return render(request,"home.html")
    

def register(request):
    if request.method=="POST":
        username = request.POST["username"]
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        alternateContact = request.POST['alternateContact']
        free = request.POST['option']
        pro = request.POST['option1']
        accountType = request.POST["accountType"]
        
        if(free=="" and pro=="pro"):
            accountFeatures = "pro"
        else:
            accountFeatures = "free"

        newUser = {
            'username' : username,
            'first_name' : fname,
            'last_name' : lname,
            'email' : email,
            'password' : pswd,
            'contact' : contact,
            'alternate_contact' : alternateContact,
            'gender' : gender,
            'account_type' : accountType,
            'account_features' : accountFeatures,
            'address' : address,
            'dob' : dob,
            'email_verified' : False
        }

        users.insert_one(newUser)
    
        user = User.objects.create_user(username=username , email=email , password=pswd)
        user.first_name = fname
        user.last_name = lname
        user.is_active = False
        user.save()
        messages.success(request,"You have successfully registered please login to continue")
        return redirect("login")

     
    return render(request,"register.html")

def login_main(request):
    
    
    if request.method=="POST":
        global user_logged
        username = request.POST["username"]
        pwd = request.POST["pwd"]

        user = auth.authenticate(username = username,password=pwd)
        user_logged_in = users.find_one({'username':user.username})
        user_logged = user_logged_in
        print(f"user = {user_logged_in} and {user_logged}")

        if user is not None:
            auth.login(request,user)
            print(user)
            messages.success(request,"Logged In successfully")
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("login")
        

        
    else: 

        return render(request,"login.html")

def contact(request):
    pass

def about(request):
    pass


def dashboard(request):
    global user_logged
    print(request.user,user_logged)
    userType = user_logged['account_type']
    if(userType=="student"):
        return render(request,"student/home.html")
    elif(userType=="teacher"):
        return render(request,"teacher/home.html")
    elif(userType=="developer"):
        return render(request,"developer/home.html")

def logout_main(request):
    global user_logged
    auth.logout(request)
    user_logged = False
    messages.success(request,"Successfully logged Out")
    return render(request,"login.html")


