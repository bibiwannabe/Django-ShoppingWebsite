# coding=utf-8
from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('shopping_user.UserInfo')
    goods = models.ForeignKey('shopping_goods.GoodsInfo')
    count = models.IntegerField()

# Create your models here.
