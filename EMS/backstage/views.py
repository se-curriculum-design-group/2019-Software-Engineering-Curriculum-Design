import os
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
import datetime
# 邮件模块
from django.conf import settings
from django.core import mail


# Create your views here.

def welcome(request):
    return render(request, 'Welcome.html')  # 引入欢迎页


def login(request):  # 用户登录验证函数
    if request.session.get('user_is_login', None):  # 如果用户在session中存在记录，则跳过登录认证程序进入主页
        return redirect('backstage:Homepage')

    if request.method == "POST":  # 若request的类型为POST，即前端表单返回数据。
        login_form = forms.UserForm(request.POST)  # 取UserForm表单数据
        message = "请检查填写的内容！(验证码)"
        if login_form.is_valid():  # 验证输入数据的类型合法性
            username = login_form.cleaned_data['username']  # 取出前端用户名输入框中输入的用户名
            password = login_form.cleaned_data['password']  # 取出前端密码输入框中输入的用户名
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                message = "welcome back!"
                return render(request, 'Homepage.html', locals())
            elif user is None:
                message = "用户不存在"
                return render(request, 'Login.html', locals())
            else:
                # 登陆失败
                print(user)
                message = "密码错误，请重试！"
                return render(request, 'Login.html', locals())
        return render(request, 'Login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'Login.html', locals())


def log_out(request):
    if not request.session.get('user_is_login', None):  # 原本未登录则无登出
        return redirect("backstage:welcome")

    request.session.flush()  # 清空所有session

    return redirect("backstage:welcome")  # 重定向到欢迎页


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            print(123)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = models.User.objects.create_user(username=username, password=password, email=email)
            user_profile = models.UserProfile(user=user, codename=username)
            user_profile.save()
            message = "注册成功"
    else:
        form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': form})


def homepage(request):
    if not request.session.get('user_is_login', None):
        return redirect('backstage:login')

    if request.method == "GET":
        announcement_all = models.Announcement.objects.filter(visible=True, receiver="全体成员")  # 取全员广播
        announcement_department = models.Announcement.objects.filter(visible=True,
                                                                     receiver=request.session.get('user_department',
                                                                                                  None),
                                                                     year=request.session.get('user_start_year',
                                                                                              None))  # 取部门年级广播
        announcement = announcement_all | announcement_department  # 通知消息队列
        return render(request, 'Homepage.html', locals())
