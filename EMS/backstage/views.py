import os
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404

from backstage.models import Student, Teacher, User, Announcement, College, AdmClass, Major, UploadFiles
from backstage.forms import *
from utils import make_encode
# 邮件模块
from django.conf import settings
from django.core import mail
from courseScheduling.models import ClassRoom, Course


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
        try:
            user = User.objects.get(username=username, password=password)
            login(request, user)
            if user.is_superuser:
                save_session('管理员')
                return redirect('backstage:admin_view')
            elif len(username) == 10:
                user = Student.objects.get(username=username)
                save_session('学生')
                return redirect('backstage:student_view')
            elif len(user.username) == 9:
                user = Teacher.objects.get(username=username)
                save_session('教师')
                return redirect('backstage:teacher_view')
            else:
                return redirect("backstage:goto_login")
        except:
            return redirect("backstage:goto_login")


@login_required
def student_view(request):
    if request.method == "GET":
        username = request.session.get('username', False)
        user = Student.objects.get(username=username)
        x = str(user.in_cls)
        department = College.objects.get(major__short_name=x[:2])
        usi = user.in_year
        announcement = Announcement.objects.filter(receiver=department, year=usi)
        announcements_to_all = Announcement.objects.filter(receiver="全体成员")
        announcements = announcement | announcements_to_all
        return render(request, 'student_base.html', locals())
    else:
        anno_id = request.POST.get('details')
        announcement = Announcement.objects.get(id=anno_id)
        return render(request, 'backstage/anno_details.html', locals())


@login_required
def admin_view(request):
    if request.method == "GET":
        announcements = Announcement.objects.all()
        adm_operator = Adm()
        return render(request, 'adm_base.html', locals())
    elif "search" in request.POST:
        adm_operator = Adm(request.POST)
        if adm_operator.is_valid():
            receivers = adm_operator.cleaned_data['receiver']
            year = adm_operator.cleaned_data['year']
            announcements = Announcement.objects.filter(receiver=receivers, year=year)
            adm_operator = Adm()
            return render(request, 'adm_base.html', locals())
        else:
            return render(request, 'errors/403page.html')
    else:
        anno_id = request.POST.get('details')
        announcement = Announcement.objects.get(id=anno_id)
        adm_operator = Adm()
        return render(request, 'backstage/adm_base_emails_details.html', locals())


@login_required
def teacher_view(request):
    if request.method == "GET":
        announcements = Announcement.objects.all()
        adm_operator = Adm()
        return render(request, 'teacher_base.html', locals())
    elif "search" in request.POST:
        adm_operator = Adm(request.POST)
        if adm_operator.is_valid():
            receivers = adm_operator.cleaned_data['receiver']
            year = adm_operator.cleaned_data['year']
            announcements = Announcement.objects.filter(receiver=receivers, year=year)
            adm_operator = Adm()
            return render(request, 'teacher_base.html', locals())
        else:
            return render(request, 'errors/403page.html')
    else:
        anno_id = request.POST.get('details')
        announcement = Announcement.objects.get(id=anno_id)
        adm_operator = Adm()
        return render(request, 'backstage/adm_base_emails_details.html', locals())


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
            # print("输入修改值为空，返回主页")
            if len(username) == 10:
                return render(request, 'student_base.html')
            else:
                return render(request, 'teacher_base.html')


def check_announcement(request):
    if request.method == "GET":
        username = request.session.get('username', False)
        user = User.objects.get(username=username)
        if user.is_superuser:
            announcements = Announcement.objects.all()
            return render(request, 'backstage/announcement_check.html', locals())


def send_announcement(request):
    if request.method == "GET":
        add_announcement = AddAnnouncement()
        return render(request, 'backstage/announcement_operate.html', locals())
    else:
        new_announcement = AddAnnouncement(request.POST)
        username = request.session.get('username', False)
        if new_announcement.is_valid():
            new_announcement_receiver = new_announcement.cleaned_data['receiver']
            new_announcement_year = new_announcement.cleaned_data['year']
            new_announcement_title = new_announcement.cleaned_data['title']
            new_announcement_text = request.POST.get('editor')
            new_announcement_objects = Announcement.objects.create()
            new_announcement_objects.title = new_announcement_title
            new_announcement_objects.messages = new_announcement_text
            new_announcement_objects.author = username
            new_announcement_objects.receiver = new_announcement_receiver
            new_announcement_objects.year = new_announcement_year
            new_announcement_objects.visible = True
            new_announcement_objects.save()
            add_announcement = AddAnnouncement()
            return render(request, 'backstage/announcement_operate.html', locals())
        else:
            add_announcement = AddAnnouncement()
            message = "表单错误"
            return render(request, 'backstage/announcement_operate.html', locals())


def send_emails(request):
    if request.method == "GET":
        new_email = SendEmails()
        return render(request, "backstage/send_emails.html", locals())
    else:
        Emailform = SendEmails(request.POST, request.FILES)
        if Emailform.is_valid():

            path = os.getcwd()
            path_use = path.replace('\\', '/')

            receivers = Emailform.cleaned_data['receiver']
            title = Emailform.cleaned_data['title']
            text = request.POST.get('editor')
            files = request.FILES.getlist('attach')
            username = request.session.get('username', False)
            for files in request.FILES.getlist('attach'):
                record = UploadFiles(file=files, author=username)
                record.save()

            recipient_list = ['18811610600@163.com']
            # if receivers == '0':
            #     users = models.User.objects.all()
            #     for user in users:
            #         recipient_list.append(user.email)
            # else:
            #     users = models.User.objects.filter(department__in=receivers)
            #     for user in users:
            #         recipient_list.append(user.email)

            from_mail = settings.EMAIL_HOST_USER
            msg = mail.EmailMessage(title, text, from_mail, recipient_list)
            msg.content_subtype = "html"
            for files in request.FILES.getlist('attach'):
                src = path_use + '/backstage/media/files/' + files.name
                msg.attach_file(src)
            if msg.send():
                message = "发送成功"
                return render(request, 'backstage/send_emails.html', locals())
            else:
                message = "发送失败"
                return render(request, 'backstage/send_emails.html', locals())


def adm_view_all_stu(request):
    if request.method == "POST":
        if "delete" in request.POST:
            username = request.POST["delete"]
            try:
                change_user = User.objects.get(username=username)
                change_user.delete()
            except:
                return render(request, 'adm_base.html', locals())

            username = request.session['username']
            adm = User.objects.get(username=username)
            if not adm.is_superuser:
                return render(request, 'errors/403page.html')
            all_college = College.objects.all()
            all_major = Major.objects.all()
            all_students = Student.objects.all()
            all_in_year = all_students.values("in_year").order_by("in_year").distinct()

            context = {
                'all_college': all_college,
                'all_major': all_major,
                'all_in_year': all_in_year,
                'all_students': all_students
            }
            return render(request, "backstage/adm_view_all_stu.html", context)
        elif "change" in request.POST:
            username = request.POST["change"]
            request.session['choose_user'] = username
            try:
                user = Student.objects.get(username=username)
            except:
                return render(request, 'adm_base.html', locals())
            return render(request, 'backstage/adm_change_stu.html', locals())
        else:
            new_password = request.POST.get('Password')
            new_name = request.POST.get('name')
            new_in_cls = request.POST.get('in_cls')
            new_score_got = request.POST.get('score_got')
            username = request.session.get('choose_user', False)

            try:

                user_op = Student.objects.get(username=username)
                new_in_class_num = AdmClass.objects.get(name=new_in_cls)

                if new_password != "":
                    change_user = User.objects.get(username=username)
                    change_user.password = make_encode(new_password)
                    change_user.save()

                user_op.in_cls = new_in_class_num
                user_op.score_got = new_score_got
                user_op.name = new_name
                user_op.save()
                user = Student.objects.get(username=username)
                return render(request, 'backstage/adm_change_stu.html', locals())
            except:
                return JsonResponse({})
    else:
        username = request.session['username']
        adm = User.objects.get(username=username)
        if not adm.is_superuser:
            return render(request, 'errors/403page.html')
        all_college = College.objects.all()
        all_major = Major.objects.all()
        all_students = Student.objects.all()
        all_in_year = all_students.values("in_year").order_by("in_year").distinct()

        context = {
            'all_college': all_college,
            'all_major': all_major,
            'all_in_year': all_in_year,
            'all_students': all_students
        }
        return render(request, "backstage/adm_view_all_stu.html", context)


def adm_view_all_teacher(request):
    if request.method == "POST":
        if "delete" in request.POST:
            username = request.POST["delete"]
            try:
                change_user = User.objects.get(username=username)
                change_user.delete()
            except:
                return render(request, 'adm_base.html', locals())

            username = request.session['username']
            adm = User.objects.get(username=username)
            if not adm.is_superuser:
                return render(request, 'errors/403page.html')
            all_college = College.objects.all()
            all_teacher = Teacher.objects.all()
            all_in_year = all_teacher.values("in_year").order_by("in_year").distinct()

            context = {
                'all_college': all_college,
                'all_in_year': all_in_year,
                'all_teacher': all_teacher
            }
            return render(request, "backstage/adm_view_all_teachers.html", context)
        elif "change" in request.POST:
            username = request.POST["change"]
            request.session['choose_user'] = username
            try:
                user = Teacher.objects.get(username=username)
                college_id = user.college_id
                college_name = College.objects.get(id=college_id).name
            except:
                return render(request, 'adm_base.html', locals())
            return render(request, 'backstage/adm_change_tea.html', locals())
        elif "add" in request.POST:
            return render(request, 'backstage/adm_add_tea.html', locals())
        elif "confirm_add" in request.POST:
            new_password = request.POST.get('Password')
            new_name = request.POST.get('name')
            new_username = request.POST.get('username')
            sex = request.POST.get('sex')
            college_name = request.POST.get('college_name')
            new_in_year = request.POST.get('in_year')
            new_title = request.POST.get('title')
            new_edu_background = request.POST.get('edu_background')
            print(123)
            try:
                college_id_for_new = College.objects.get(name=college_name).id
                print(123)
                if sex == "男":
                    sex_int = 1
                else:
                    sex_int = 0
                new_tea = Teacher.objects.create(password=new_password, username=new_username,
                                                 edu_background=new_edu_background, title=new_title,
                                                 in_year=new_in_year, college=college_id_for_new, sex=sex_int)
                print(123)
                new_tea.save()
            except:
                return render(request, 'adm_base.html', locals())
        else:
            new_password = request.POST.get('Password')
            new_name = request.POST.get('name')
            college_name = request.POST.get('college_name')
            new_in_year = request.POST.get('in_year')
            new_title = request.POST.get('title')
            new_edu_background = request.POST.get('edu_background')
            username = request.session.get('choose_user', False)
            try:

                user_op = Teacher.objects.get(username=username)

                new_college = College.objects.get(name=college_name)

                if new_password != "":
                    change_user = User.objects.get(username=username)
                    change_user.password = make_encode(new_password)
                    change_user.save()

                user_op.college_id = new_college
                user_op.title = new_title
                user_op.name = new_name
                user_op.in_year = new_in_year
                user_op.edu_background = new_edu_background
                user_op.save()
                user = Teacher.objects.get(username=username)
                return render(request, 'backstage/adm_change_tea.html', locals())
            except:
                return JsonResponse({})
    else:
        username = request.session['username']
        adm = User.objects.get(username=username)
        if not adm.is_superuser:
            return render(request, 'errors/403page.html')
        all_college = College.objects.all()
        all_teacher = Teacher.objects.all()
        all_in_year = all_teacher.values("in_year").order_by("in_year").distinct()

        context = {
            'all_college': all_college,
            'all_in_year': all_in_year,
            'all_teacher': all_teacher
        }
        return render(request, "backstage/adm_view_all_teachers.html", context)


def adm_view_all_class_room(request):
    username = request.session['username']
    adm = User.objects.get(username=username)
    if not adm.is_superuser:
        return render(request, 'errors/403page.html')
    all_class_room = ClassRoom.objects.all()
    context = {
        'all_class_room': all_class_room
    }
    return render(request, "backstage/adm_view_all_classroom.html", context)


def adm_view_all_course(request):
    username = request.session['username']
    adm = User.objects.get(username=username)
    if not adm.is_superuser:
        return render(request, 'errors/403page.html')
    all_course = Course.objects.all()
    all_college = College.objects.all()
    all_course_type = all_course.values("course_type").distinct()
    context = {
        'all_course': all_course,
        'all_college': all_college,
        'all_course_type': all_course_type,
    }
    return render(request, "backstage/adm_view_all_course.html", context)
