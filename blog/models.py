from django.db import models
import datetime

# Create your models here.

class BlogPost(models.Model):
    blog_id = models.AutoField
    user_name = models.CharField(max_length = 1000)
    title = models.CharField(max_length=1000)
    article = models.CharField(max_length = 999999999999999)
    category = models.CharField(max_length = 1000)
    publish_date = models.DateField(default = datetime.date.today)
    image = models.ImageField(upload_to = "blog/images")

    def __str__(self):
        return self.title
