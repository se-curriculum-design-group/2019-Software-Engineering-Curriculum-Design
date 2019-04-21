import os
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404


from backstage.models import Student, Teacher, User
from utils import make_encode


def welcome(request):
    name = request.session['name']
    user_type = request.session['user_type']
    context = {
        'name': name,
        'user_type': user_type
    }
    return render(request, 'base.html', context)


def goto_login(request):
    return render(request, 'login.html')


@csrf_exempt
def mylogin(request):

    def save_session(user_type):
        request.session['username'] = username
        request.session['name'] = user.name
        request.session['password'] = password
        request.session['user_type'] = user_type

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 对密码进行加密
        password = make_encode(password)
        if 10 == len(username):
            # 学号的长度是10位
            try:
                user = Student.objects.get(username=username, password=password)
                login(request, user)
                save_session('学生')
                return redirect('backstage:welcome')
            except:
                return JsonResponse({})
        elif 9 == len(username):
            try:
                user = Student.objects.get(username=username, password=password)
                login(request, user)
                save_session('学生')
                return redirect('backstage:welcome')
            except:
                return JsonResponse({})
        else:
            try:
                user = User.objects.get(username=username, password=password)
                login(request, user)
                save_session('管理员')
                return redirect('backstage:welcome')
            except:
                return JsonResponse({})


@login_required
def student_view(request):
    return render(request, 'student_base.html')


@login_required
def admin_view(request):
    return render(request, 'adm_base.html')


@login_required
def teacher_view(request):
    return render(request, 'teacher_base.html')


@login_required
def mylogout(request):
    logout(request)
    return render(request, 'base.html')


@login_required
def register(request):
    raise NotImplemented
