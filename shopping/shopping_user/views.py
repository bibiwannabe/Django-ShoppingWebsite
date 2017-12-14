# coding='utf-8'
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from . import user_decorator
from .models import *
from hashlib import sha1
from . import models



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

def register_exist(request):
    username = request.GET.get('username')
    count = models.UserInfo.objects.filter(username=username).count()
    return JsonResponse({'count':count})

def login(request):
    username=request.COOKIES.get('username', '')
    context={'title':'用户登录','error_name': 0,'error_pwd': 0,'username': username}
    return render(request, 'shopping_user/login.html',context)

def login_handle(request):
    post = request.POST
    username = post.get('username')
    userpassword = post.get('pwd')
    remember = post.get('jizhu',0)
    users = UserInfo.objects.filter(username=username)
    #print(username)
    if len(users)==1:
        print(username)
        s1=sha1()
        s1.update(str(userpassword).encode('utf-8'))
        if s1.hexdigest()==users[0].userpassword:
            url = request.COOKIES.get('url','/')#从cookie中取出url完整路径参照user_decorator
            red = HttpResponseRedirect(url)
            #记住用户名
            if remember!=0:
                red.set_cookie('username',username)
            else:
                red.set_cookie('username','',max_age=-1)#max_age：过期时间
            request.session['user_id'] = users[0].id#用于user_decorator传用户id验证是否登录
            request.session['user_name'] = username
            return red
        else:
            context = {'title':'用户登录','error_name': 0,'error_pwd': 1,'username': username,'userpassword':userpassword}
            return render(request,'shopping_user/login.html',context)
    else:
        context = {'title':'用户登录','error_name': 1,'error_pwd': 0,'username': username,'userpassword':userpassword}
        return render(request,'shopping_user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

#request.session['user_name'] = username
@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).useremail
    context = {'title':'用户中心',
               'user_email':user_email,
               'user_name':request.session['user_name']}
    return render(request,'shopping_user/user_center_info.html',context)

@user_decorator.login
def order(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    context = {'title':'用户中心',
               'user':user}
    return render(request,'shopping_user/user_center_order.html',context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        user.userreseive = request.POST.get('name')
        user.useradd = request.POST.get('add')
        user.useryoubian = request.POST.get('youbian')
        user.userphone = request.POST.get('phone_number')
        user.save()

    context ={'title':'用户中心',
             'user':user,
              }
    return render(request,'shopping_user/user_center_site.html',context)