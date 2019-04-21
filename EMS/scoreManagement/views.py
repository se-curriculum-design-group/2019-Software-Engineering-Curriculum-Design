from django.shortcuts import render, redirect
from django.http import HttpResponse

from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from scoreManagement.models import Course, MajorPlan, MajorCourses


def welcome(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    colleges = College.objects.all()
    majors = Major.objects.all()
    major_plans = MajorPlan.objects.all()
    class_rooms = ClassRoom.objects.all()

    context = {
        'students': students,
        'teachers': teachers,
    }
    return render(request, 'scoreManage/adm_score_manage.html', context)


def score_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'scoreManage/student_score_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'scoreManage/student_score_manage.html')
    else:
        return render(request, 'scoreManage/adm_score_manage.html')
