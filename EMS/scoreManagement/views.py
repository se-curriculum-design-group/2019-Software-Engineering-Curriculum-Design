from django.shortcuts import render, redirect
from django.http import HttpResponse

from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from scoreManagement.models import Course, MajorPlan, MajorCourses, CourseScore


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


def adm_all_course_score(request):
    all_course_score = CourseScore.objects.all()[:10]
    first_course_score = CourseScore.objects.first()

    context = {'all_course_score': all_course_score}
    return render(request, 'scoreManage/adm_score_manage.html', context)


def score_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'scoreManage/student_score_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'scoreManage/teacher_score_manage.html')
    else:
        return render(request, 'scoreManage/adm_score_manage.html')
