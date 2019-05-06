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
def student_choose_project(request):
	return render(request,'graduationManagement/student_choose_project.html')

def teacher_edit_project(request):
	return render(request,'graduationManagement/teacher_edit_project.html')

def student_submit_project(request):
	return render(request,'graduationManagement/student_submit_project.html')

def student_view_score(request):
	return render(request,'graduationManagement/student_view_score.html')
