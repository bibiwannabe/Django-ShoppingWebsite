# coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1

def register(request):
    return render(request,'shopping_user/register.html')

def register_handle(request):
    post = request.POST
    username = post.get('user_name')
    userpassword=post.get('pwd')
    cuserpassword = post.get('cpwd')
    useremail = post.get('email')
    if userpassword != cuserpassword:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(str(userpassword).encode('utf-8'))
    upwd = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.username = username
    print(username)
    user.userpassword = upwd
    user.useremail = useremail
    user.save()
    return redirect('/user/login/')

