import os
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
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
        if user_type == '管理员':
            request.session['name'] = username
        else:
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
                return redirect('backstage:student_view')
            except:
                return redirect('backstage:goto_login')
                # return JsonResponse({"not_exist": "1"})
        elif 9 == len(username):
            try:
                user = Teacher.objects.get(username=username, password=password)
                login(request, user)
                save_session('教师')
                return redirect('backstage:teacher_view')
            except:
                return redirect("backstage:goto_login")
                # return JsonResponse({"not_exist": "1"})
        else:
            try:
                user = User.objects.get(username=username, password=password)
                login(request, user)
                save_session('管理员')
                return redirect('backstage:admin_view')
            except:
                return redirect("backstage:goto_login")
                # return JsonResponse({"not_exist": "1"})


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


def backstage_manage(request):
    return render(request, 'backstage/adm_backstage_manage.html')


@login_required
def register(request):
    raise NotImplemented


def my_personal_details(request):
    if request.method == "GET":
        username = request.session.get('username', False)
        if len(username) == 10:
            try:
                user = Student.objects.get(username=username)
                return render(request, 'backstage/my_personal_details.html', locals())
            except:
                return JsonResponse({})
        else:
            try:
                user = Teacher.objects.get(username=username)
                return render(request, 'backstage/my_personal_details_teacher.html', locals())
            except:
                return JsonResponse({})
    else:
        new_password = request.POST.get('Password')
        username = request.session.get('username', False)
        if new_password != "":
            if len(username) == 10:
                try:
                    user = Student.objects.get(username=username)
                    change_user = User.objects.get(username=username)
                    change_user.password = make_encode(new_password)
                    change_user.save()
                    return render(request, 'backstage/my_personal_details.html', locals())
                except:
                    return JsonResponse({})
            else:
                try:
                    user = Teacher.objects.get(username=username)
                    change_user = User.objects.get(username=username)
                    change_user.password = new_password
                    change_user.save()
                    return render(request, 'backstage/my_personal_details_teacher.html', locals())
                except:
                    return JsonResponse({})
        else:
            print("输入修改值为空，返回主页")
            if len(username) == 10:
                return render(request, 'student_base.html')
            else:
                return render(request, 'teacher_base.html')
