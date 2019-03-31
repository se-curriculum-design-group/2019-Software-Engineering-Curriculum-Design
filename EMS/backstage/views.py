import os
from django.shortcuts import render, redirect
from . import models
from . import forms
import datetime
# 邮件模块
from django.conf import settings
from django.core import mail


# Create your views here.

def welcome(request):
    return render(request, 'Welcome.html')  # 引入欢迎页


def login(request):
    if request.session.get('user_is_login', None):
        return redirect('backstage:homepage')

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！(验证码)"

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = models.User.objects.filter(codename=username)
            if user:
                user = user.first()
                if user.password == password:
                    request.session['user_is_login'] = True
                    request.session['user_codename'] = user.codename
                    request.session['user_nickname'] = user.nickname
                    request.session['user_department'] = user.department_id
                    request.session['user_grant'] = user.grant
                    request.session['user_start_year'] = user.start_year
                    message = "你好，欢迎回来！"
                    return redirect('backstage:Homepage')
                    # return render(request, 'homepage.html', locals())
                else:
                    message = "密码不正确！"
            else:
                message = "用户不存在!"
                return render(request, 'Welcome.html', locals())
        return render(request, 'Login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'Login.html', locals())


def log_out(request):
    if not request.session.get('user_is_login', None):  # 原本未登录则无登出
        return redirect("backstage:welcome")

    request.session.flush()  # 清空所有session

    return redirect("backstage:welcome")  # 重定向到欢迎页


def register(request):
    return


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
