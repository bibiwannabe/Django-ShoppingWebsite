from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    userpassword = models.CharField(max_length=40)
    useremail = models.CharField(max_length=30)
    userreseive = models.CharField(max_length=20)
    useradd = models.CharField(max_length=100)
    useryoubian = models.CharField(max_length=6)
    userphone = models.CharField(max_length=11)