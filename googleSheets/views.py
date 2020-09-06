#importing the necessary package for handling google sheets
from django.shortcuts import render , redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.image import MIMEImage  
from email import encoders
from django.contrib import messages
import os


#defining scopes
scope = [
    
]



#getting the credentials
creds = #get your credentials here




client = gspread.authorize(creds)
sheet = client.open('form_response').sheet1
responses = sheet.get_all_records()

# Create your views here.

def showResponse(request):    
    
    global responses
    global sheet
    
    sheet = client.open('form_response').sheet1
    responses = sheet.get_all_records()

    
    
    return render(request,"googleSheets/home.html" , {"responses":responses , "isActive":True})

def sendMail(request,email,row):
    global responses
    global sheet
    row = int(row)

    files = [
        
    ]

    col_count = len(responses[0])

    mail = MIMEMultipart()
    mail['From'] = "youremail@xyz.xom"
    mail["To"] = email
    mail['Subject'] = "No-Reply"

    message = f"""Thankyou {email} to send your response.
    This is just a simple project.
    Your Response is Accepted.
    You will get a glimpse of this with the attachments send with this email.
    Thanking you"""

    mail.attach(MIMEText(message,"plain"))

    for file in files:
        file_data = open(file, 'rb').read()
        file_to_send = MIMEImage(file_data, name=os.path.basename(file))
        mail.attach(file_to_send)
    
    smtp_session = smtplib.SMTP('smtp.gmail.com' , 587)

    smtp_session.starttls()

    smtp_session.login("youremail@email.com" , "yourpassword")

    try:
        smtp_session.sendmail("email@email.com",email,mail.as_string())
        messages.success(request,"Message successfully send.....")
        smtp_session.quit()
        sheet.update_cell(row+1,col_count-1 , "TRUE")
        sheet.update_cell(row+1,col_count , "TRUE")

    except:
        messages.error(request,"Invalid email address....")

    return redirect("showResponse")

def dontSendMail(request,email,row):
    global responses
    global sheet
    row = int(row)

    files = [

    ]

    col_count = len(responses[0])
    
    
    smtp_session = smtplib.SMTP('smtp.gmail.com' , 587)

    smtp_session.starttls()

    smtp_session.login("youremail@email.com" , "yourpassword")
    mail = MIMEMultipart()
    mail['From'] = "your email"
    mail["To"] = email
    mail['Subject'] = "No-Reply"

    message = f"""Thankyou {email} to send your response.
    This is just a simple project.
    Sorry but your Response is not Accepted.
    You will get a glimpse of this with the attachments send with this email.
    Thanking you"""

    mail.attach(MIMEText(message,"plain"))

    for file in files:
        file_data = open(file, 'rb').read()
        file_to_send = MIMEImage(file_data, name=os.path.basename(file))
        mail.attach(file_to_send)

    try:
        smtp_session.sendmail("email",email,mail.as_string())
        messages.success(request,"Message successfully send.....")
        smtp_session.quit()
        sheet.update_cell(row+1,col_count-1 , "TRUE")
        sheet.update_cell(row+1,col_count , "FALSE")

    except:
        messages.error(request,"Invalid email address....")

    return redirect("showResponse")

    

    


    
