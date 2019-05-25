from django.shortcuts import render
from courseScheduling.Schedule import *

def welcome(request):
    exam_schedule()
    return render(request, 'courseScheduing/welcome.html')


def scheduling_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseScheduing/student_scheduling_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseScheduing/teacher_scheduling_manage.html')
    else:
        return render(request, 'courseScheduing/adm_scheduling_manage.html')


def time_exam(request):
    return render(request, "courseScheduing/time_exam.html")