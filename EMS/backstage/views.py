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
            user = auth.authenticate(username=username, password=password)  # 在父类用户表中匹配输入

            if user is not None and user.is_active:  # 若在父类用户表中找到并该用户活跃
                auth.login(request, user)
                user_is_teacher = models.Teacher.objects.filter(code=username)  # 尝试在teacher子表中查找，更小若预测错误开销更小
                if user_is_teacher.first() is None:  # 若不在教师表中则在学生表中
                    user_is_student = models.Student.objects.get(code=username)  # 尝试在student子表中查找
                    request.session['user_is_login'] = True  # 将登录信息存入session
                    request.session['user_code'] = user_is_student.code  # 传入编号
                    request.session['user_name'] = user_is_student.name  # 传入姓名
                    request.session['user_department'] = user_is_student.department_id  # 传入部门
                else:
                    request.session['user_is_login'] = True  # 将登录信息存入session
                    request.session['user_code'] = user_is_teacher.code  # 传入编号
                    request.session['user_name'] = user_is_teacher.name  # 传入姓名
                    request.session['user_department'] = user_is_teacher.department_id  # 传入部门
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


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)  # 调起RegistrationForm注册表单
        if form.is_valid():
            usercode = form.cleaned_data['username']  # 提取各项表单数据
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            age = form.cleaned_data['age']
            start_year = form.cleaned_data['start_year']
            length = form.cleaned_data['length']
            major = form.cleaned_data['major']
            major_id = models.Major.objects.filter(name=major).first()
            print(major_id.id)
            user = models.User.objects.create_user(username=usercode, password=password, email=email,
                                                   first_name=name)  # 在父类User中构建新对象
            user_Student = models.Student(user=user, code=usercode, name=name, sex=sex, age=age,
                                          start_year=start_year,
                                          major_id=major_id.id)  # 在子类学生表中构建新对象
            user_Student.save()  # 存入数据库
            return redirect('backstage:login')  # 重定向到登录
        message = "请修改输入"
        return render(request, 'register.html', locals())
    else:
        form = forms.RegistrationForm()  # 调起表单
    return render(request, 'register.html', {'form': form})


def register_t(request):  # 对老师用户的注册，开发测试使用，请优先使用脚本生成必要数据
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)  # 调起TeacherForm注册表单
        if form.is_valid():
            usercode = form.cleaned_data['username']  # 提取各项表单数据
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            department = form.cleaned_data['department']
            user = models.User.objects.create_user(username=usercode, password=password, email=email,
                                                   first_name=name)  # 在父类User中构建新对象

            print(department)
            user_Teacher = models.Teacher(user=user, code=usercode, name=name, title=title, department_id=department)
            user_Teacher.save()
            return redirect('backstage:login')
        message = "请修改输入"
        return render(request, 'register.html', locals())
    else:
        form = forms.TeacherForm()
    return render(request, 'register.html', {'form': form})


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
