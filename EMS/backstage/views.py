import os
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from backstage.models import Student, Teacher
from utils import make_encode


def welcome(request):
    return render(request, 'base.html')


def goto_login(request):
    return render(request, 'login.html')


@csrf_exempt
def mylogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password = make_encode(password)
    print(username)
    print(password)
    if 10 == len(username):
        # 学号的长度是10位
        # user = authenticate(username=username, password=password)
        user = Student.objects.get(username=username, password=password)
        print(user.name)
        print(type(user))
    else:
        user = Teacher.objects.get(username=username, password=password)
        print(type(user))
        print(user.name)
    if user:
        login(request, user)
        context = {
            'user': user
        }
        return render(request, 'base.html', context)
    else:
        return HttpResponse("登录失败，请重试。")


def register(request):
    return render(request, 'register.html')
    pass


@login_required
def mylogout(request):
    print("-------------------------")
    logout(request)
    return render(request, 'base.html')
