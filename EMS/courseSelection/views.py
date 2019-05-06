from django.shortcuts import render


def welcome(request):
    return render(request, 'courseSelection/welcome.html')


def selection_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseSelection/student_selection_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseSelection/teacher_selection_manage.html')
    else:
        return render(request, 'courseSelection/adm_selection_manage.html')
