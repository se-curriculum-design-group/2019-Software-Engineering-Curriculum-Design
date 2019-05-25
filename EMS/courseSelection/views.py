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


def stu_major(request):
    nowtime = datetime.datetime.now()
    nowtime = str(nowtime)
    nowtime = nowtime[0:16]
    nowtime = nowtime[0:10]+'T'+nowtime[11:19]

    if((nowtime < settings.BEGIN or nowtime > settings.END ) or settings.BEGIN == 'NULL' or settings.END == 'NULL'):
        return HttpResponse("当前不是选课时间！")
    else:
        sno = request.session["username"]
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        current_semester = 0
        p = Student.objects.get(username=sno)

        majorName = p.in_cls.major.major.mname
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
        college = [c['tno__mcno__cno__college__name'] for c in mC.values("tno__mcno__cno__college__name").distinct()]
        majors = [s['tno__mcno__mno__major__mname'] for s in mC.values("tno__mcno__mno__major__mname").distinct()]

        context = {
            "mC": mC,
            "college": college,
            "majors": majors
        }
        majorC = []
        for m in mC:
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
        return render(request, "courseSelection/stu_major.html", {'data': json.dumps(data), 'dat': json.dumps(dat),'mC':mC,'college':college,'majors':majors})


def select_course(request):
    if request.is_ajax():
        if request.method == 'GET':
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
            Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)
            X = CourseSelected.objects.filter(sno__username=sno, cno_id=ID)
            X.delete()

            return JsonResponse({"flag": 1, "tot": tot, "ID": ID})

def find_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            sno = request.session["username"]
            theCourse = CourseSelected.objects.filter(sno__username=sno)
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
    mC = Teacher_Schedule_result.objects.filter()

    college = [c['tno__mcno__cno__college__name'] for c in mC.values("tno__mcno__cno__college__name").distinct()]
    majors = [s['tno__mcno__mno__major__mname'] for s in mC.values("tno__mcno__mno__major__mname").distinct()]
    context = {
        "mC": mC,
        "college": college,
        "majors": majors
    }
    return render(request, "courseSelection/adm_school.html",context)

def time_set(request):
    begin = request.POST.get('begin_time')
    settings.BEGIN = begin
    # BEGIN = begin
    # global END
    end = request.POST.get('end_time')
    settings.END = end
    return render(request, "courseSelection/adm_selection_manage.html")


def student_view_other_course(request):
    sno = request.session["username"]

    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_semester = 0
    p = Student.objects.get(username=sno)

    majorName = p.in_cls.major.major.mname
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
        if (1 <= current_month <= 2):
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
    college = [c['tno__mcno__cno__college'] for c in mC.values("tno__mcno__cno__college").distinct()]
    majors = [s['tno__mcno__mno__major__mname'] for s in mC.values("tno__mcno__mno__major__mname").distinct()]

    context = {
        "mC": mC,
        "college": college,
        "majors": majors
    }
    return render(request, "courseSelection/stu_major.html", context)
def tables(request):
    return render(request,"courseSelection/course_table.html")
def teacher(request):  # 教师查看授课选课情况
    user = request.session["username"]
    teacher = Teacher.objects.get(username=user)
    teachings = Teaching.objects.filter(tno=teacher)
    # coursescore, id, mcno, mcno_id, teacher_schedule_result, tno, tno_id, weight
    context = {
        'teachings': teachings
    }
    return render(request, "courseSelection/teacher.html", context)


def show_students(request, cno, course_type):  # 教师查看授课选课情况
    user = request.session["username"]
    teacher = Teacher.objects.get(username=user)
    class_no = Course.objects.get(cno=cno, course_type=course_type)
    major_courses = MajorCourses.objects.get(cno=class_no)
    teaching = Teaching.objects.get(mcno=major_courses, tno=teacher)
    teacher_schedule_result = Teacher_Schedule_result.objects.filter(tno=teaching)
    if not teacher_schedule_result:
        return render(request, "courseSelection/show_students.html")
    else:
        teacher_schedule_result = teacher_schedule_result[0]
    students = CourseSelected.objects.filter(cno=teacher_schedule_result)

    context = {
        'students': students
    }
    return render(request, "courseSelection/show_students.html", context)
