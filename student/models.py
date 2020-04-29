from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    email_verified = models.BooleanField()
    address = models.CharField(max_length = 500)
    contact = models.IntegerField()
    alternateContact = models.IntegerField()
    gender = models.CharField(max_length = 50)
    account_feature = models.CharField(max_length = 50)
    dob = models.DateField(default=datetime.date.today)
    profile_image = models.ImageField(upload_to = "student/images")

    def __str__(self):
        return self.username
    