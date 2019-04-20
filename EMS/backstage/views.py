import os
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404

import xml.etree.ElementTree as ET

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
    # 对密码进行加密
    password = make_encode(password)
    if 10 == len(username):
        # 学号的长度是10位
        user = get_object_or_404(Student, username=username, password=password)
    else:
        user = get_object_or_404(Teacher, username=username, password=password)
    if not user:
        if request.is_ajax():
            return JsonResponse({'no_exist': True})
    login(request, user)
    return redirect("backstage:welcome")


def register(request):
    return render(request, 'register.html')
    pass


@login_required
def mylogout(request):
    logout(request)
    return render(request, 'base.html')
