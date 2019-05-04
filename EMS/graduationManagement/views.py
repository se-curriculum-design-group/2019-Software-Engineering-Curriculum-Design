from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, 'graduationManagement/welcome.html')


def graduation_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'graduationManagement/student_graduation_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'graduationManagement/teacher_graduation_manage.html')
    else:
        return render(request, 'graduationManagement/adm_graduation_manage.html')
