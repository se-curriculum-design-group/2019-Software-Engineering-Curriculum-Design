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
    return render(request, 'scoreManage/scoreManagement.html', context)

