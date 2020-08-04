from django.urls import path , include
from . import views

urlpatterns = [
    path("" , views.showResponse , name = "showResponse"),
    path("send_mail/<email>/<row>/" , views.sendMail , name="sendMail"),
    path("dont_send_mail/<email>/<row>" , views.dontSendMail , name="dontSendMail"),
]