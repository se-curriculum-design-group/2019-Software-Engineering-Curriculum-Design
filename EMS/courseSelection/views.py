from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from courseScheduling.models import Course, MajorPlan, MajorCourses, Teaching, Teacher_Schedule_result
from courseSelection.models import CourseSelected
import json
import numpy as np
import datetime
from django.conf import settings
import pymysql


def welcome(request):
    return render(request, 'courseSelection/welcome.html')


def selection_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseSelection/student_selection_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseSelection/teacher_selection_manage.html')
    else:
        return render(request, 'courseSelection/adm_selection_manage.html')


def stu_tongshi(request):
    return render(request, "courseSelection/stu_tongshi.html")


# def stu_

def stu_major(request):
    sno = request.session["username"]

    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_semester = 0
    p = Student.objects.get(username=sno)

    majorName = p.in_cls.major.major.mname
    print(majorName)
    inyear = p.in_year

    if (current_year - inyear) == 0:
        current_semester = 1
    elif (current_year - inyear) == 1:
        if (current_month >= 1 and current_month <= 2):
            current_semester = 1
        elif (current_month > 2 and current_month <= 7):
            current_semester = 2
        elif (current_month > 7 and current_month < 9):
            current_semester = 3
        elif (current_month >= 9 and current_month <= 12):
            current_semester = 1
    elif (current_year - inyear) == 2:
        if (current_month >= 1 and current_month <= 2):
            current_semester = 1
        elif (current_month > 2 and current_month <= 7):
            current_semester = 2
        elif (current_month > 7 and current_month < 9):
            current_semester = 3
        elif (current_month >= 9 and current_month <= 12):
            current_semester = 1
    elif (current_year - inyear) == 3:
        if (current_month >= 1 and current_month <= 2):
            current_semester = 1
        elif (current_month > 2 and current_month <= 7):
            current_semester = 2
        elif (current_month > 7 and current_month < 9):
            current_semester = 3
        elif (current_month >= 9 and current_month <= 12):
            current_semester = 1
    elif (current_year - inyear) == 4:
        if (current_month >= 1 and current_month <= 2):
            current_semester = 1
        elif (current_month > 2 and current_month <= 7):
            current_semester = 2
        elif (current_month > 7 and current_month < 9):
            current_semester = 3
        elif (current_month >= 9 and current_month <= 12):
            current_semester = 1

    mC = Teacher_Schedule_result.objects.filter(
        tno__mcno__year=current_year,
        tno__mcno__semester=current_semester
    )
    majorC = []
    for m in mC:
        print(m.tno.mcno.mno.major.mname)
        if m.tno.mcno.mno.major.mname == majorName and m.state == "专业选修":
            majorC.append(m)
    data = []
    dat = []
    haveChosen = {}

    courseChosen = CourseSelected.objects.filter(sno__username=sno)

    for c in courseChosen:
        if (c.cno.state != "专业必修" and c.cno.state != "公共基础必修"):
            tmp = {}
            haveChosen[c.cno.id] = 1
            tmp["id"] = c.cno.id
            tmp["课程号"] = c.cno.tno.mcno.cno.cno
            tmp["课程名"] = c.cno.tno.mcno.cno.cname
            tmp["学时"] = c.cno.tno.mcno.hour_total
            tmp["选课人数"] = c.cno.current_number
            tmp["课程容量"] = c.cno.MAX_number
            tmp["授课教师"] = c.cno.tno.tno.name
            tmp["上课教室"] = c.cno.where.crno
            tmp["上课时间"] = c.cno.time

            dat.append(tmp)
    for major in majorC:
        tmp = {}
        try:
            if haveChosen[major.id] == 1:
                tmp["if_chosen"] = 1
        except:
            tmp["if_chosen"] = 0
        tmp["id"] = major.id
        tmp["课程号"] = major.tno.mcno.cno.cno
        tmp["课程名"] = major.tno.mcno.cno.cname
        tmp["学时"] = major.tno.mcno.hour_total
        tmp["选课人数"] = major.current_number
        tmp["课程容量"] = major.MAX_number
        tmp["授课教师"] = major.tno.tno.name
        tmp["上课教室"] = major.where.crno
        tmp["上课时间"] = major.time
        if tmp["选课人数"] < tmp["课程容量"]:
            data.append(tmp)
    return render(request, "courseSelection/stu_major.html", {'data': json.dumps(data), 'dat': json.dumps(dat)})


def select_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            print("asdasd")
            flag = 1
            ID = request.GET.get("id")
            sno = request.session["username"]
            X = np.zeros((25, 8, 14), dtype=np.int)
            confilict_candidate = CourseSelected.objects.filter(sno__username=sno)  # 选的不同的课
            tot = 0
            course_time = []  # 收集这些课程的上课时间
            for i in confilict_candidate:
                tmp = i.cno.time.split(",")  # 同一门课程在一周内不同的时间上
                for j in tmp:  # 一周内不同的天
                    dic = {}
                    district = j.split("-")
                    dic["周数"] = district[2] + "-" + district[3]
                    dic["节次"] = district[0] + "-" + district[1]
                    course_time.append(dic)
            for i in course_time:
                week = i["周数"].split("-")
                times = i["节次"].split("-")
                cstart = 0
                cend = 0
                Day = 0
                if int(times[1]) >= 1 and int(times[1]) <= 13:
                    Day = 1
                elif int(times[1]) >= 14 and int(times[1]) <= 26:
                    Day = 2
                elif int(times[1]) >= 27 and int(times[1]) <= 39:
                    Day = 3
                elif int(times[1]) >= 40 and int(times[1]) <= 52:
                    Day = 4
                elif int(times[1]) >= 53 and int(times[1]) <= 65:
                    Day = 5
                elif int(times[1]) >= 66 and int(times[1]) <= 78:
                    Day = 6
                elif int(times[1]) >= 79 and int(times[1]) <= 91:
                    Day = 7

                cstart = int(times[0]) % 13
                cend = int(times[1]) % 13

                if cstart == 0:
                    cstart = 13
                if cend == 0:
                    cend = 13
                X[int(week[0]):int(week[1]) + 1, Day, cstart:cend + 1] = 1

            stu_new = Student.objects.get(username=sno)
            teach = Teacher_Schedule_result.objects.get(id=ID)
            tmp = teach.time.split(",")
            single_course = []
            if teach.current_number >= teach.MAX_number:
                flag = 3
                return JsonResponse(
                    {"flag": flag, "tot": tot})
            else:
                for j in tmp:
                    dic = {}
                    district = j.split("-")
                    dic["周数"] = district[2] + "-" + district[3]
                    dic["节次"] = district[0] + "-" + district[1]
                    single_course.append(dic)

                for j in single_course:
                    week = j["周数"].split("-")
                    times = j["节次"].split("-")
                    cstart = 0
                    cend = 0
                    Day = 0
                    if int(times[1]) >= 1 and int(times[1]) <= 13:
                        Day = 1
                    elif int(times[1]) >= 14 and int(times[1]) <= 26:
                        Day = 2
                    elif int(times[1]) >= 27 and int(times[1]) <= 39:
                        Day = 3
                    elif int(times[1]) >= 40 and int(times[1]) <= 52:
                        Day = 4
                    elif int(times[1]) >= 53 and int(times[1]) <= 65:
                        Day = 5
                    elif int(times[1]) >= 66 and int(times[1]) <= 78:
                        Day = 6
                    elif int(times[1]) >= 79 and int(times[1]) <= 91:
                        Day = 7

                    cstart = int(times[0]) % 13
                    cend = int(times[1]) % 13
                    if cstart == 0:
                        cstart = 13
                    if cend == 0:
                        cend = 13

                    if np.sum(X[int(week[0]):int(week[1]) + 1, Day, cstart:cend + 1]) != 0:
                        flag = 0
                        print(flag)
                        break

                if (flag):
                    new_cord = CourseSelected()
                    new_cord.sno = stu_new
                    new_cord.cno = teach
                    new_cord.score = 0
                    new_cord.save()
                    tot = teach.current_number
                    tot += 1
                    Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)

                return JsonResponse(
                    {"flag": flag, "tot": tot})


def delete(request):
    if request.is_ajax():
        if request.method == 'GET':
            ID = request.GET.get("id")
            sno = request.session["username"]
            teach = Teacher_Schedule_result.objects.get(id=ID)

            tot = teach.current_number
            tot -= 1
            print(ID)
            Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)
            X = CourseSelected.objects.filter(sno__username=sno, cno_id=ID)
            X.delete()

            return JsonResponse({"flag": 1, "tot": tot, "ID": ID})


# def search(request):
# if request.method == 'GET':
# request.GET.get[]


def find_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            sno = request.session["username"]
            theCourse = CourseSelected.objects.filter(sno__username=sno)
            print(theCourse)
            course_time = []  # 收集这些课程的上课时间
            dic = {}
            tmp = {}
            t_info = {}
            t_place = {}
            for i in theCourse:  # 每门课
                tmp = i.cno.time.split(",")  # 同一门课程在一周内不同的时间上
                t_info[i.cno.tno.mcno.cno.cname] = i.cno.tno.tno.name
                t_place[i.cno.tno.mcno.cno.cname] = i.cno.where.crno
                dic[i.cno.tno.mcno.cno.cname] = []
                for j in tmp:  # 一周内不同的天
                    tp = {}
                    district = j.split("-")
                    tp["周数"] = district[2] + "-" + district[3]
                    tp["节次"] = district[0] + "-" + district[1]
                    dic[i.cno.tno.mcno.cno.cname].append(tp)
            return JsonResponse({"dic": dic, "t_info": t_info, "t_place": t_place})


def adm_selection_manage(request):
    return render(request, "courseSelection/adm_selection_manage.html")


def adm_class(request):
    return render(request, "courseSelection/adm_class.html")


def adm_school(request):
    return render(request, "courseSelection/adm_school.html")


def school_query(request):
    time = request.POST.get("time")
    grade = request.POST.get("grade")
    college = request.POST.get("college")
    subject = request.POST.get("subject")

    print(time, grade, college, subject)
    db = pymysql.connect("localhost", "EMS", "password", "ems", charset='utf8')
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * FROM course")

    # 使用 fetchone() 方法获取一条数据

    results = cursor.fetchall()
    n = 0
    # print(results)
    final_id = 0
    final_cno = 0
    final_cname = ""
    final_ctype = ""
    final_cscore = 0
    final_college = 0
    target = "CSE32500C"
    for row in results:
        id1 = row[0]
        cno = row[1]
        cname = row[2]
        typ = row[3]
        score = row[4]
        college = row[5]
        n += 1
        if cno == target:
            final_id = id1
            final_cno = cno
            final_cname = cname
            final_college = college
            final_cscore = score
            final_ctype = typ
            break

    cursor.execute("SELECT * FROM college")
    print(final_college)

    # cursor.execute("SELECT name,short_name FROM college WHERE id > %s",final_college)

    results = cursor.fetchall()
    # print(results)
    for row in results:
        id1 = row[0]
        if id1 == final_college:
            print(row[1], row[2])
            break
    # print(n)
    # print(final_cname)

    # 关闭数据库连接
    db.close()
    label_list = ["计科", "自动化", "电子信息"]  # 各部分标签
    size = [75, 35, 10]  # 各部分大小

    color = ["red", "green", "blue"]  # 各部分颜色
    explode = [0.05, 0, 0]  # 各部分突出值

    return render(request, "courseSelection/adm_showimg.html")


def class_query(request):
    time = request.POST.get("time")
    grade = request.POST.get("grade")
    college = request.POST.get("college")
    subject = request.POST.get("subject")
    print(time, grade, college, subject)
    return render(request, "courseSelection/adm_classshow.html")


def time_set(request):
    '''
    print(12334)
    if request.method == 'POST':
        print('sdas')
    if request.is_ajax():
        print(12324)
        if request.method == 'POST':
            print(323)
    print(request)
    '''
    print('test1')
    print(settings.BEGIN)
    begin = request.POST.get('begin_time')
    settings.BEGIN = begin
    print('test2')
    print(settings.BEGIN)
    # BEGIN = begin
    # global END
    end = request.POST.get('end_time')
    settings.END = end
    return render(request, "courseSelection/adm_selection_manage.html")
