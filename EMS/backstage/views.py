import os
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib import auth
from random import choice
from django.contrib.auth.hashers import make_password, check_password
import datetime
# 邮件模块
from django.conf import settings
from django.core import mail


# Please Create your views here.

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
            user = auth.authenticate(username=username, password=password)  # 在父类用户表中匹配输入

            if user is not None and user.is_active:  # 若在父类用户表中找到并该用户活跃
                auth.login(request, user)
                user_is_teacher = models.Teacher.objects.filter(tno=username)  # 尝试在teacher子表中查找，更小若预测错误开销更小
                if user_is_teacher.first() is None:  # 若不在教师表中则在学生表中
                    user_is_student = models.Student.objects.get(sno=username)  # 尝试在student子表中查找
                    request.session['user_is_login'] = True  # 将登录信息存入session
                    request.session['user_code'] = user_is_student.sno  # 传入编号
                    request.session['user_name'] = user_is_student.username  # 传入姓名
                    # request.session['user_department'] = user_is_student.department_id  # 传入部门
                else:
                    request.session['user_is_login'] = True  # 将登录信息存入session
                    request.session['user_code'] = user_is_teacher.tno  # 传入编号
                    request.session['user_name'] = user_is_teacher.username  # 传入姓名
                    request.session['user_department'] = user_is_teacher.college  # 传入部门
                return redirect('backstage:homepage')  # 重定向到主页
            elif user is None:  # 如果用户不存在反馈前端信息
                message = "用户不存在"
                return render(request, 'Login.html', locals())
            else:  # 密码错误情况判断逻辑
                # 登陆失败
                message = "密码错误，请重试！"
                return render(request, 'Login.html', locals())
        return render(request, 'Login.html', locals())

    login_form = forms.UserForm()  # 调起表单传到前端等待输入
    return render(request, 'Login.html', locals())


def log_out(request):
    if not request.session.get('user_is_login', None):  # 原本未登录则无登出
        return redirect("backstage:welcome")

    request.session.flush()  # 清空所有session

    return redirect("backstage:welcome")  # 重定向到欢迎页


def homepage(request):  # 主页
    if not request.session.get('user_is_login', None):  # 若用户登录信息缺失，重定向到登录页
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



