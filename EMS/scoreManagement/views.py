from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
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
    return render(request, 'scoreManage/student_score_manage.html', context)


def adm_all_course_score(request):
    all_course_score = CourseScore.objects.all()[:20]

    print(len(all_course_score))
    context = {"all_course_score": all_course_score}
    return render(request, 'scoreManage/adm_score_manage.html', context)


def score_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'scoreManage/student_score_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'scoreManage/teacher_score_manage.html')
    else:
        return render(request, 'scoreManage/adm_score_manage.html')


def std_view_major_course(request):
    sno = request.session['username']
    student = Student.objects.get(username=sno)
    # my_major_plan = student.in_cls.major
    all_major_course = MajorCourses.objects.all()
    all_college = College.objects.all()
    all_course_type = Course.objects.values("course_type").distinct()
    all_year = MajorCourses.objects.values("year").order_by("year").distinct()
    all_major = Major.objects.all()
    context = {"all_major_course": all_major_course,
               "all_college": all_college,
               "all_course": all_course_type,
               "all_year": all_year,
               "student": student,
               "all_major": all_major
               }
    return render(request, "scoreManage/student_major_course.html", context)


def std_view_major_plan(request):
    sno = request.session['username']
    student = Student.objects.get(username=sno)
    all_major_plan = MajorPlan.objects.all()
    all_college = College.objects.all()
    all_year = MajorPlan.objects.values("year").order_by("year").distinct()
    college_id = request.GET.get('stat_type_id', None)
    all_major = Major.objects.all()
    context = {
        "all_major_plan": all_major_plan,
        "all_college": all_college,
        "all_year": all_year,
        "student": student,
        "all_major": all_major
    }
    return render(request, "scoreManage/student_major_plan.html", context)


def _ajax(request):
    print(request.GET['year'])
    data = {"yes": True}
    return JsonResponse(data)
