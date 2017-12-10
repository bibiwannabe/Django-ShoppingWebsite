#coding=utf-8
from django.db import models

class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    userpassword = models.CharField(max_length=40)
    useremail = models.CharField(max_length=30)
    userreseive = models.CharField(max_length=20,default='')
    useradd = models.CharField(max_length=100,default='')
    useryoubian = models.CharField(max_length=6,default='')
    userphone = models.CharField(max_length=11,default='')