from django.shortcuts import render, redirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
import json

from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass, User
from scoreManagement.models import Teaching, Course, MajorPlan, MajorCourses, CourseScore, EvaluationForm


def welcome(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    print(teachers)

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
    if request.session['user_type'] == '管理员':
        all_course_score = CourseScore.objects.all()
        context = {"all_course_score": all_course_score}
        return render(request, 'scoreManage/adm_score_manage.html', context)
    else:
        return Http404()


def score_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'scoreManage/student_score_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'scoreManage/teacher_score_manage.html')
    else:
        return render(request, 'scoreManage/adm_score_manage.html')


def student_score(request):
    if request.session['user_type'] != '学生':
        redirect("scoreManagement:welcome")
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
        redirect("scoreManagement:welcome")
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
        redirect("scoreManagement:welcome")
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
    if request.session['user_type'] != '学生':
        return redirect("scoreManagement:welcome")
    if request.GET:
        item_sno = request.session['username']
        # 学生对象
        student = Student.objects.get(username=item_sno)
        # 更改评价表的is_finish字段
        EvaluationForm.objects.filter(student=student).update(is_finish=True)
        return redirect('scoreManagement:assess_teacher')


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
    return render(request, "scoreManage/teacher_view_teaching.html", context)


# 授课老师录入成绩
def teacher_upload_score(request):
    if request.session['user_type'] != '教师':
        return render(request, 'errors/403page.html')
    tno = request.session['username']
    teacher = Teacher.objects.get(username=tno)
    my_courses = Teaching.objects.filter(tno=teacher)
    return render(request, 'scoreManage/teacher_upload_score.html')
