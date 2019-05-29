from django.shortcuts import render, redirect, Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime

import pandas as pd

from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass, User
from courseScheduling.models import Teaching, Course, MajorPlan, MajorCourses, Teacher, Teacher_Schedule_result
from courseSelection.models import CourseSelected
from scoreManagement.models import CourseScore, EvaluationForm

from .utils import get_semester


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
    try:
        username = request.session['username']
        adm = User.objects.get(username=username)
        if not adm.is_superuser:
            return render(request, 'errors/403page.html')
        else:
            all_colleges = College.objects.all()
            all_majors = Major.objects.all()
            all_course_score = CourseSelected.objects.filter(is_finish=True)
            all_years = [y['teaching__mcno__year'] for y in
                         CourseScore.objects.values("teaching__mcno__year").distinct()]
            all_semester = [y['teaching__mcno__semester'] for y in
                            CourseScore.objects.values("teaching__mcno__semester").distinct()]
            try:
                sear_year = request.GET['sear_year']
                sear_semester = request.GET['sear_semester']
                tch_sch_list = Teacher_Schedule_result.objects.filter(tno__mcno__year=sear_year, tno__mcno__semester=sear_semester)
                all_course_score = CourseSelected.objects.filter(cno__in=tch_sch_list)
                context = {
                    "all_course_score": all_course_score,
                    "all_years": all_years,
                    "all_semester": all_semester,
                    "all_colleges": all_colleges,
                    "all_majors": all_majors,
                    "sear_year": sear_year,
                    "sear_semester": sear_semester,
                }
                return render(request, 'scoreManage/adm_score_manage.html', context)
            except Exception:
                context = {
                    "all_course_score": all_course_score,
                    "all_years": all_years,
                    "all_semester": all_semester,
                    "all_colleges": all_colleges,
                    "all_majors": all_majors,
                }
                return render(request, 'scoreManage/adm_score_manage.html', context)
    except:
        return render(request, 'errors/500page.html')


def score_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'scoreManage/student_score_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'scoreManage/teacher_score_manage.html')
    else:
        return render(request, 'scoreManage/adm_score_manage.html')


def student_view_score(request):
    if request.session['user_type'] != '学生':
        return render(request, 'errors/403page.html')
    sno = request.session['username']
    student = Student.objects.get(username=sno)
    course_score = CourseScore.objects.filter(sno=student)
    years = [c['teaching__mcno__year'] for c in course_score.values("teaching__mcno__year").distinct()]
    semesters = [s['teaching__mcno__semester'] for s in course_score.values("teaching__mcno__semester").distinct()]
    context = {
        "my_course_score": course_score,
        "years": years,
        "semesters": semesters
    }
    return render(request, "scoreManage/student_view_score.html", context)


def student_own_study(request):
    if request.session['user_type'] != '学生':
        redirect("scoreManagement:welcome")
    sno = request.session['username']
    student = Student.objects.get(username=sno)
    course_list = \
        CourseScore.objects.filter(sno=student). \
            order_by("teaching__mcno__year", "teaching__mcno__semester")
    year_semester = \
        course_list.values_list("teaching__mcno__year", "teaching__mcno__semester"). \
            distinct()
    # 总学分
    sum = Student.objects.get(username=sno).score_got
    # 毕业所需学分
    sum_req = student.in_cls.major.score_grad
    # 总绩点
    gpa = 0
    for course_list_item in course_list:
        a = course_list_item.teaching.mcno.cno.score
        b = course_list_item.score
        if b >= 90:
            gpa = gpa + a / sum * 4
        elif 80 <= b < 90:
            gpa = gpa + a / sum * 3
        elif 70 <= b < 80:
            gpa = gpa + a / sum * 2
        elif 60 <= b < 70:
            gpa = gpa + a / sum * 1
        else:
            gpa = gpa

    # 每个学期的平均绩点
    semester_GPA_list = []
    # 每个学期的总学分
    semester_sum_list = []
    # 每个学期选课的数量
    semester_num_list = []
    for year_semester_item in year_semester:
        semester_course = \
            course_list.filter(
                Q(teaching__mcno__year=year_semester_item[0]),
                Q(teaching__mcno__semester=year_semester_item[1])
            )
        semester_num_list.append(semester_course.count())
        semester_sum = 0
        semester_GPA = 0
        for year_semester_course_item in semester_course:
            a = year_semester_course_item.teaching.mcno.cno.score
            semester_sum = semester_sum + a
        semester_sum_list.append(semester_sum)
        for year_semester_course_item in semester_course:
            a = year_semester_course_item.teaching.mcno.cno.score
            b = year_semester_course_item.score
            if b >= 90:
                semester_GPA = semester_GPA + a / semester_sum * 4
            elif 80 <= b < 90:
                semester_GPA = semester_GPA + a / semester_sum * 3
            elif 70 <= b < 80:
                semester_GPA = semester_GPA + a / semester_sum * 2
            elif 60 <= b < 70:
                semester_GPA = semester_GPA + a / semester_sum * 1
            else:
                semester_GPA = semester_GPA
        semester_GPA_list.append(semester_GPA)
    context = {
        "student_name": student.name,
        "my_scoresum": sum,
        "my_gpa": round(gpa, 2),
        "my_year_semester": year_semester,
        "semester_GPA": semester_GPA_list,
        "semester_scoresum": semester_sum_list,
        "my_score_gg": sum_req,
        "my_score_g": round(sum / sum_req, 2),
        "semester_num": semester_num_list,
    }
    return render(request, "scoreManage/student_own_study.html", context)


def std_view_major_course(request):
    if request.session['user_type'] != '学生':
        return render(request, 'errors/403page.html')
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
    if request.session['user_type'] != '学生':
        return render(request, 'errors/403page.html')
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


def teacher_view_major_course(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    all_major_course = MajorCourses.objects.all()
    all_college = College.objects.all()
    all_course_type = Course.objects.values("course_type").distinct()
    all_year = MajorCourses.objects.values("year").order_by("year").distinct()
    all_major = Major.objects.all()
    context = {"all_major_course": all_major_course,
               "all_college": all_college,
               "all_course": all_course_type,
               "all_year": all_year,
               "all_major": all_major
               }
    return render(request, "scoreManage/teacher_major_course.html", context)


def teacher_view_major_plan(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    all_major_plan = MajorPlan.objects.all()
    all_college = College.objects.all()
    all_year = MajorPlan.objects.values("year").order_by("year").distinct()
    all_major = Major.objects.all()
    context = {
        "all_major_plan": all_major_plan,
        "all_college": all_college,
        "all_year": all_year,
        "all_major": all_major
    }
    return render(request, "scoreManage/teacher_major_plan.html", context)


def adm_view_major_course(request):
    username = request.session['username']
    adm = User.objects.get(username=username)
    if not adm.is_superuser:
        return render(request, 'errors/403page.html')
    all_major_plan = MajorPlan.objects.all()
    all_course = Course.objects.all()
    all_major_course = MajorCourses.objects.all()
    all_college = College.objects.all()
    all_course_type = Course.objects.values("course_type").distinct()
    all_year = MajorCourses.objects.values("year").order_by("year").distinct()
    all_major = Major.objects.all()
    context = {"all_major_course": all_major_course,
               "all_college": all_college,
               "all_course_type": all_course_type,
               "all_year": all_year,
               "all_major": all_major,

               "all_major_plan": all_major_plan,
               "all_course": all_course,
               }
    return render(request, "scoreManage/adm_major_course.html", context)


def adm_view_major_plan(request):
    username = request.session['username']
    adm = User.objects.get(username=username)
    if not adm.is_superuser:
        return render(request, 'errors/403page.html')
    all_major_plan = MajorPlan.objects.all()
    all_college = College.objects.all()
    all_year = MajorPlan.objects.values("year").order_by("year").distinct()
    all_major = Major.objects.all()
    context = {
        "all_major_plan": all_major_plan,
        "all_college": all_college,
        "all_year": all_year,
        "all_major": all_major
    }
    return render(request, "scoreManage/adm_major_plan.html", context)


# 学生评教
def assess_teacher(request):
    if request.session['user_type'] != '学生':
        redirect("scoreManagement:welcome")

    # 判断该学生是否已经全部提交过
    def judge(s):
        items = EvaluationForm.objects.filter(student_id=s)
        if len(items) != 0:
            for item in items:
                if item.is_finish == False:
                    return False  # 该学生还未提交
                else:
                    return True  # 该学生已经提交
        else:
            return False

    log = []
    stuno = request.session['username']
    sno_id = stuno[4:]  # 得到学生id
    stu = Student.objects.filter(username=stuno)
    courses = CourseScore.objects.filter(sno=sno_id)  # 从选课表中找出该学生修的课程
    num1 = 0
    sum = 0
    for item1 in courses:
        teachings = Teaching.objects.filter(id=item1.teaching_id)
        for item2 in teachings:
            if item2.mcno.year == 2017 and item2.mcno.semester == 1:
                # print(item2)
                # print(item2.tno.name)
                # print(item2.mcno.cno.cname)
                # print(item2.mcno.cno.course_type)
                temp = dict()
                temp['student'] = stuno
                temp['sno'] = stu  # 学生
                temp['cno'] = item2.mcno.cno  # 课程
                # print(item2.mcno.cno)
                temp['course'] = item2.mcno.id
                temp['tno'] = item2.tno  # 教师
                temp['teacher'] = item2.tno_id
                # print(item2.tno_id)
                temp['state'] = False
                temp['r1'] = 0
                temp['r2'] = 0
                temp['r3'] = 0
                temp['r4'] = 0
                temp['r5'] = 0
                temp['r6'] = 0
                temp['r7'] = 0
                temp['r8'] = 0
                temp['text'] = "无"
                temp['flag'] = False
                try:
                    temp1 = EvaluationForm.objects.get(
                        student_id=sno_id, course_id=item2.mcno.id, teacher_id=item2.tno_id)
                    temp['r1'] = temp1.item1
                    temp['r2'] = temp1.item2
                    temp['r3'] = temp1.item3
                    temp['r4'] = temp1.item4
                    temp['r5'] = temp1.item5
                    temp['r6'] = temp1.item6
                    temp['r7'] = temp1.item7
                    temp['r8'] = temp1.item8
                    temp['text'] = temp1.description
                    temp['flag'] = temp1.is_finish
                    # print("!!!")
                    # if temp1.is_finish == True:
                    temp['state'] = True
                    num1 += 1
                except:
                    temp['state'] = False
                    # print("???")
                    pass

                temp['tname'] = item2.tno.name
                temp['cname'] = item2.mcno.cno.cname
                # print(item2.tno.id)
                temp['type'] = item2.mcno.cno.course_type
                # if temp1.is_finish == True:
                #     temp['state'] = "提交"
                # else:
                #     temp['state'] = "未提交"
                sum += 1
                log.append(temp)
    # print(log)
    num2 = sum - num1
    flag = judge(sno_id)
    context = {'log': log, 'num1': num1, 'num2': num2, 'flag': flag}

    return render(request, 'scoreManage/assess_teacher.html', context=context)


# 学生提交评价信息
def submit_result(request):
    if request.session['user_type'] != '学生':
        redirect("scoreManagement:welcome")
    print("!!!")

    # 得到各个等级对应的分数
    def getScore(s):
        if s == 'A':
            return 100
        elif s == 'B':
            return 90
        elif s == 'C':
            return 70
        elif s == 'D':
            return 60
        elif s == 'E':
            return 50

    # if 'submit_result' in request.POST:
    if request.GET:
        r1 = request.GET.get('r1')
        r2 = request.GET.get('r2')
        r3 = request.GET.get('r3')
        r4 = request.GET.get('r4')
        r5 = request.GET.get('r5')
        r6 = request.GET.get('r6')
        r7 = request.GET.get('r7')
        r8 = request.GET.get('r8')
        text = request.GET.get('message')
        if text == "":
            text = "无"
        item_sno = request.GET.get('item_sno')
        item_tno = request.GET.get('item_tno')
        item_cno = request.GET.get('item_cno')

        r1 = getScore(r1)
        r2 = getScore(r2)
        r3 = getScore(r3)
        r4 = getScore(r4)
        r5 = getScore(r5)
        r6 = getScore(r6)
        r7 = getScore(r7)
        r8 = getScore(r8)
        print(r1, r2, r3, r4, r5, r6, r7, r8, text)
        sum = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
        ave = sum * 1.0 / 8
        # print(ave)
        # print(type(item_sno), type(item_tno), type(item_cno))
        # 学生对象
        student = Student.objects.get(username=item_sno)
        # print(student)
        # 教师对象
        # print(item_tno)
        teacher = Teacher.objects.get(id=item_tno)
        # print(teacher)
        # 课程对象
        course = MajorCourses.objects.get(id=item_cno)
        # print(course)
        print("!!!")
        try:
            EvaluationForm.objects.get(
                student=student, course=course, teacher=teacher)
            EvaluationForm.objects.filter(student=student, course=course, teacher=teacher).update(
                item1=r1, item2=r2, item3=r3, item4=r4, item5=r5, item6=r6, item7=r7, item8=r8, description=text,
                sum=ave, is_finish=False)
        except:
            EvaluationForm.objects.create(student=student, course=course, teacher=teacher, item1=r1, item2=r2,
                                          item3=r3, item4=r4, item5=r5, item6=r6, item7=r7, item8=r8, description=text,
                                          sum=ave, is_finish=False)
        return redirect('scoreManagement:assess_teacher')


# # 最终的提交，提交后不可更改
@csrf_exempt
def submit_all(request):
    try:
        if request.session['user_type'] != '学生':
            return render(request, 'errors/403page.html')
        if request.GET:
            item_sno = request.session['username']
            # 学生对象
            student = Student.objects.get(username=item_sno)
            # 更改评价表的is_finish字段
            EvaluationForm.objects.filter(student=student).update(is_finish=True)
            return redirect('scoreManagement:assess_teacher')
    except:
        return render(request, 'errors/500page.html')


def teacher_view_teaching(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    teaching_list = Teaching.objects.filter(tno=teacher)
    years = [y['mcno__year'] for y in teaching_list.values('mcno__year').distinct()]
    semesters = [s['mcno__semester'] for s in teaching_list.values('mcno__semester').distinct()]
    context = {
        'teaching_list': teaching_list,
        'years': years,
        'semesters': semesters
    }

    if request.method == 'GET':
        try:
            other_tno = request.GET['seacher_tno']
        except MultiValueDictKeyError:
            return render(request, "scoreManage/teacher_view_teaching.html", context)
        try:
            other_teacher = Teacher.objects.get(username=other_tno)
        except Teacher.DoesNotExist:
            return render(request, "scoreManage/teacher_view_teaching.html", context)
        other_teaching_list = Teaching.objects.filter(tno=other_teacher)
        other_years = [y['mcno__year'] for y in other_teaching_list.values('mcno__year').distinct()]
        other_semesters = [s['mcno__semester'] for s in other_teaching_list.values('mcno__semester').distinct()]
        result = {
            "is_find": True,
            "other_tno": other_tno,
            "other_years": other_years,
            "other_semesters": other_semesters,
            "other_teaching_list": other_teaching_list,
            'teaching_list': teaching_list,
            'years': years,
            'semesters': semesters
        }
        return render(request, "scoreManage/teacher_view_teaching.html", result)
    return render(request, "scoreManage/teacher_view_teaching.html", context)


# 授课老师录入成绩
def teacher_upload_score(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    my_courses = Teaching.objects.filter(tno=teacher)
    return render(request, 'scoreManage/teacher_upload_score.html')


# 管理员查看教学评价情况
def adm_view_teacher_evaluation(request):
    username = request.session['username']
    adm = User.objects.get(username=username)
    if not adm.is_superuser:
        return render(request, 'errors/403page.html')
    evaluation_sets = EvaluationForm.objects.all()
    context = {
        'evaluation_sets': evaluation_sets
    }
    return render(request, 'scoreManage/adm_view_teacher_evaluation.html', context)


# 获取到老师教的课
def get_all_teaching(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    this_year = datetime.now().year
    this_semester = get_semester(datetime.now().month)
    teaching_list = Teaching.objects.filter(tno=teacher, mcno__year=this_year, mcno__semester=this_semester)
    tch_sch_list = Teacher_Schedule_result.objects.filter(tno__in=teaching_list)

    all_year = [year[0] for year in teaching_list.values_list('mcno__year').distinct()]
    all_semester = [semester[0] for semester in teaching_list.values_list('mcno__semester').distinct()]

    context = {
        'teaching_list': teaching_list,
        'tch_sch_list': tch_sch_list,
        'all_year': all_year,
        'all_semester': all_semester,
        'this_year': this_year,
        'this_semester': this_semester,
    }
    return render(request, 'scoreManage/teacher_view_stu_score.html', context)


def show_student_score(request, cno, course_type):
    user = request.session["username"]
    teacher = Teacher.objects.get(username=user)
    class_no = Course.objects.get(cno=cno, course_type=course_type)
    major_courses = MajorCourses.objects.get(cno=class_no)
    teaching = Teaching.objects.get(mcno=major_courses, tno=teacher)
    teacher_schedule_result = Teacher_Schedule_result.objects.filter(tno=teaching)
    if not teacher_schedule_result:
        return render(request, "scoreManage/tch_view_stu_score_detail.html")
    else:
        teacher_schedule_result = teacher_schedule_result[0]
    course_selected = CourseSelected.objects.filter(cno=teacher_schedule_result)
    adm_id_list = course_selected.values('sno__in_cls').distinct()
    adm_class_list = []
    for adm_id in adm_id_list:
        adm_class_list.append(AdmClass.objects.get(id=adm_id['sno__in_cls']))
    context = {
        'course_selected': course_selected,
        'adm_class_list': adm_class_list
    }
    return render(request, "scoreManage/tch_view_stu_score_detail.html", context)


def teacher_view_stu_score(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    if request.method == 'GET':
        try:
            year = request.GET['year']
            semester = request.GET['semester']
            if year == '无' or semester == '无':
                return render(request, 'scoreManage/teacher_view_stu_score.html')
            teaching_list = Teaching.objects.filter(tno=teacher, mcno__year=year, mcno__semester=semester)
        except MultiValueDictKeyError:
            year = datetime.now().year
            month = datetime.now().month
            if month == 7:
                semester = 3
            elif 3 <= month <= 6:
                semester = 2
            else:
                semester = 1
            teaching_list = Teaching.objects.filter(tno=teacher, mcno__year=year, mcno__semester=semester)
        else:
            year = datetime.now().year
            month = datetime.now().month
            if month == 7:
                semester = 3
            elif 3 <= month <= 6:
                semester = 2
            else:
                semester = 1
            teaching_list = Teaching.objects.filter(tno=teacher, mcno__year=year, mcno__semester=semester)

    all_teaching_list = Teaching.objects.filter(tno=teacher)
    schedule_result = Teacher_Schedule_result.objects.filter(tno__in=teaching_list)
    course_list = CourseSelected.objects.filter(cno__in=schedule_result)
    adm_id_list = course_list.values('sno__in_cls').distinct()
    adm_class_list = []
    for adm_id in adm_id_list:
        adm_class_list.append(AdmClass.objects.get(id=adm_id['sno__in_cls']))

    all_year = [year[0] for year in all_teaching_list.values_list('mcno__year').distinct()]
    all_semester = [semester[0] for semester in all_teaching_list.values_list('mcno__semester').distinct()]

    context = {
        'course_list': course_list,
        'adm_class_list': adm_class_list,
        'all_year': all_year,
        'all_semester': all_semester,
        'teaching_list': teaching_list,
    }
    return render(request, 'scoreManage/teacher_view_stu_score.html', context)


def adm_change_score(request):
    if request.is_ajax():
        if len(request.GET):
            year = request.GET.get('year')
            semester = request.GET.get('semester')
            college = request.GET.get('college')
            major = request.GET.get('major')
            sno = request.GET.get('sno')
            tno = request.GET.get('tno')
            cno = request.GET.get('cno')
            method = request.GET.get('method')
            common = request.GET.get('common')
            final_score = request.GET.get('final')
            student = Student.objects.get(username=sno)
            teacher = Teacher.objects.get(username=tno)
            try:
                course = Course.objects.get(cno=cno, course_type=method)
                major_course = MajorCourses.objects.get(cno=course, year=year, semester=semester)
                teaching = Teaching.objects.get(tno=teacher, mcno=major_course)
                course_score = CourseScore.objects.get(sno=student, teaching=teaching)
            except Course.MultipleObjectsReturned or CourseScore.MultipleObjectsReturned:
                return JsonResponse({"except": Exception})

            course_score.commen_score = common
            course_score.final_score = final_score
            weight = course_score.teaching.weight
            course_score.score = float(common) * (1 - weight) + float(final_score) * weight
            course_score.save()

            n_commen = common
            n_final = final_score
            score = course_score.score
            result = {
                'n_commen': n_commen,
                'n_final': n_final,
                'score': score,
            }
            return JsonResponse(result)
    return redirect("scoreManagement:adm_all_course_score")


def adm_change_major_plan(request):
    if request.is_ajax():
        if len(request.GET):
            year = request.GET.get('year')
            major_name = request.GET.get('major')
            people_num = request.GET.get('people_num')
            lowest_score = request.GET.get('lowest_score')
            stu_method = request.GET.get('stu_method')
            course_num = request.GET.get('course_num')
            adm_class_num = request.GET.get('adm_class_num')

            major = Major.objects.get(mno=major_name.split('-')[0])
            major_plan = MajorPlan.objects.get(major=major, year=year)
            # make change
            major_plan.cls_num = adm_class_num
            major_plan.people_num = people_num
            major_plan.score_grad = lowest_score
            major_plan.stu_years = stu_method
            major_plan.course_num = course_num
            major_plan.save()
            new_people_num = major_plan.people_num
            new_score_grad = major_plan.score_grad
            new_clsw_num = major_plan.cls_num
            new_stu_years = major_plan.stu_years
            new_course_num = major_plan.course_num

            data = {
                'new_people_num': new_people_num,
                'new_score_grad': new_score_grad,
                'new_clsw_num': new_clsw_num,
                'new_stu_years': new_stu_years,
                'new_course_num': new_course_num,
            }
            return JsonResponse(data)


# 管理员修改专业课程，只修改部分属性
def adm_change_major_course(request):
    if request.is_ajax():
        if len(request.GET):
            major = request.GET.get('major')
            year = request.GET.get('year')
            semester = request.GET.get('semester')
            cno = request.GET.get('cno')
            teach_hours = request.GET.get('teach_hours')
            exp_hours = request.GET.get('exp_hours')
            exam_method = request.GET.get('exam_method')

            major_plan = MajorPlan.objects.get(major__mno=major.split('-')[1], year=major.split('-')[0])
            # 获取到MajorCourse对象
            print(cno)
            major_course = MajorCourses.objects.get(cno__cno=cno, mno=major_plan)
            major_course.year = year
            major_course.semester = semester
            major_course.hour_class = teach_hours
            major_course.hour_other = exp_hours
            major_course.hour_total = teach_hours + exp_hours
            major_course.exam_method = (exam_method == '考试')

            major_course.save()
            return JsonResponse({})


# 管理员添加专业课程信息
def adm_add_major_course(request):
    if request.is_ajax():
        if len(request.GET):
            major_str = request.GET.get('major_str').split('-')
            year = request.GET.get('year')
            semester = request.GET.get('semester')
            major_course = request.GET.get('major_course')
            teach_hour = request.GET.get('teach_hour')
            exp_hour = request.GET.get('exp_hour')
            hour_total = teach_hour + exp_hour
            exam_method = request.GET.get('exam_method')
            exam_method = (exam_method == '考试')
            major = MajorPlan.objects.get(major__mno=major_str[1], year=major_str[0])
            course = Course.objects.filter(cno=major_course)[0]
            MajorCourses.objects.update_or_create(
                cno=course,
                mno=major,
                year=year,
                semester=semester,
                hour_total=hour_total,
                hour_class=teach_hour,
                hour_other=exp_hour,
                exam_method=exam_method
            )
            return JsonResponse({})


# 管理员删除专业课程MajorCourse信息
def adm_delete_major_course(request):
    if request.is_ajax():
        if len(request.GET):
            major_plan_str = request.GET.get('major_plan').split('-')
            cno = request.GET.get('cno')
            ctype = request.GET.get('ctype')
            course = Course.objects.get(cno=cno, course_type=ctype)
            major_plan = MajorPlan.objects.get(year=major_plan_str[0], major__mno=major_plan_str[1])
            major_course = MajorCourses.objects.get(cno=course, mno=major_plan)
            major_course.delete()
            return JsonResponse({})


# 管理员添加课程Course
def adm_add_course(request):
    if request.is_ajax():
        if len(request.GET):
            add_college = request.GET.get('add_college')
            cno = request.GET.get('cno')
            cname = request.GET.get('cname')
            ctype = request.GET.get('ctype')
            cscore = request.GET.get('cscore')
            college = College.objects.get(name=add_college)
            Course.objects.update_or_create(cno=cno, cname=cname, college=college, course_type=ctype, score=cscore)
            return JsonResponse({})


# 管理员修改课程Course
def adm_change_course(request):
    if request.is_ajax():
        if len(request.GET):
            cno = request.GET.get('cno')
            ctype = request.GET.get('ctype')
            n_op_college = request.GET.get('n_op_college')
            n_cno = request.GET.get('n_cno')
            n_cname = request.GET.get('n_cname')
            n_ctype = request.GET.get('n_ctype')
            n_cscore = request.GET.get('n_cscore')
            course = Course.objects.get(cno=cno, course_type=ctype)
            try:
                college = College.objects.get(name=n_op_college)
                course.college = college
                course.course_type = n_ctype
                course.cno = n_cno
                course.cname = n_cname
                course.score = n_cscore
                course.save()
            except College.DoesNotExist:
                return JsonResponse({"exception": '学院不存在'})
            return JsonResponse({})


# 管理员删除课程Course
def adm_delete_course(request):
    if request.is_ajax():
        if len(request.GET):
            cno = request.GET.get('cno')
            ctype = request.GET.get('ctype')
            cname = request.GET.get('cname')
            try:
                course = Course.objects.get(cno=cno, course_type=ctype, cname=cname)
                course.delete()
            except Course.DoesNotExist:
                print(cno, ctype, cname)
            return JsonResponse({})


# 获取到老师教了并且排了的课
def get_all_course_selected(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    this_year = datetime.now().year
    this_semester = get_semester(datetime.now().month)
    teaching_list = Teaching.objects.filter(tno=teacher, mcno__year=this_year, mcno__semester=this_semester)
    tch_sch_list = Teacher_Schedule_result.objects.filter(tno__in=teaching_list)

    all_year = [year[0] for year in teaching_list.values_list('mcno__year').distinct()]
    all_semester = [semester[0] for semester in teaching_list.values_list('mcno__semester').distinct()]

    context = {
        'teaching_list': teaching_list,
        'tch_sch_list': tch_sch_list,
        'all_year': all_year,
        'all_semester': all_semester,
        'this_year': this_year,
        'this_semester': this_semester,
    }
    return render(request, 'scoreManage/teacher_upload_score.html', context)


def upload_student_score(request, tch_sch_id):
    tch_sch = Teacher_Schedule_result.objects.get(id=tch_sch_id)
    weight = tch_sch.tno.weight
    course_selected_list = CourseSelected.objects.filter(cno_id=tch_sch_id)
    context = {
        'course_selected_list': course_selected_list,
        'weight': weight,
        'tch_sch': tch_sch_id,
    }
    return render(request, "scoreManage/tch_upload_score_detail.html", context)


# 教师添加单个学生成绩
def tch_add_score(request):
    if request.is_ajax():
        if len(request.GET):
            cs_id = request.GET.get('cs_id')
            com_score = float(request.GET.get('com_score'))
            fin_score = float(request.GET.get('fin_score'))
            weight = float(request.GET.get('weight'))
            cs = CourseSelected.objects.get(id=cs_id)
            cs.common_score = com_score
            cs.final_score = fin_score
            cs.score = com_score * (1 - weight) + fin_score * weight
            score = round(cs.score, 2)
            cs.is_finish = True
            cs.save()
            return JsonResponse({"score": score})


# 修改成绩权重
def tch_change_score_weight(request):
    if request.is_ajax():
        if len(request.GET):
            old_weight = float(request.GET.get('old_weight'))
            final_weight = float(request.GET.get('final_weight'))
            tch_sch_id = request.GET.get('tch_sch_id')

            print(old_weight, final_weight)

            if old_weight == final_weight:
                return JsonResponse({"no_need": "yes"})

            course_selected_list = CourseSelected.objects.filter(cno_id=tch_sch_id)
            course_selected_list[0].cno.tno.weight = final_weight
            course_selected_list[0].cno.tno.save()

            for c in course_selected_list:
                c.cno.tno.weight = final_weight
                c.cno.tno.save()
                c.score = c.common_score * (1 - final_weight) + c.final_score * final_weight
                c.save()
            return JsonResponse({"succ": "yes"})


# 处理批量上传的文件
@csrf_exempt
def handle_batch_score(request):
    if request.method == 'POST':
        f = request.FILES.get('fileUpload')
        excel_data = pd.read_excel(f)
        excel_data.columns = excel_data.iloc[0]
        excel_data = excel_data.drop(0)
        tch_id = 0
        try:
            for _, row in excel_data.iterrows():
                cs_id, sno, comm, final, wei = row['编号'], row['学号'], row['平时分'], row['考试分'], row['考试权重']
                cs = CourseSelected.objects.get(id=cs_id)
                tch_id = cs.cno_id
                cs.common_score = comm
                cs.final_score = final
                cs.score = comm * (1 - wei) + final * wei
                cs.is_finish = True
                cs.save()
        except:
            return render(request, "errors/500page.html")
        return redirect("scoreManagement:upload_student_score", tch_id)
