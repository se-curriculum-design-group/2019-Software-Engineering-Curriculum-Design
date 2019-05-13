from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from scoreManagement.models import Course, MajorPlan, MajorCourses, CourseScore,Teaching
from courseScheduling.models import Teacher_Schedule_result
from courseSelection.models import CourseSelected
import json
import numpy as np

def welcome(request):
    return render(request, 'courseSelection/welcome.html')
# def resultAdd(request):
#     teaching = Teaching.objects.all()
#     for i in teaching:
#         new_cord = Teacher_Schedule_result()
#         new_cord.tno = i
#         # new_cord.contain_num = 19
#         new_cord.current_number = 0
#         new_cord.MAX_number = 190
#         new_cord.time = "1-2-4-5,2-6-7-8"
#         # new_cord.crtype ="阶教"
#         # new_cord.crno="A阶-104"
#
#         new_cord.state="无"
#         new_cord.save()
#
#     # new_cord = Teacher_Schedule_result()
#     # new_cord.tno = teaching
#     # new_cord.time = "1-2-4-5, 2-6-7-8"
#     # new_cord.crtype = "阶教"
#     # new_cord.crno = "A阶-104"
#     # new_cord.contain_num = 190
#     # new_cord.current_number = 0
#     # new_cord.MAX_number = 190
#     # new_cord.state = "无"
#     # new_cord.save()
#
#     student = Student.objects.all()
#     plan = MajorPlan.objects.all()
#     for j in plan:
#         print(j)
#     print("asdasd")
#     for i in student:
#         print(i.in_cls)
#     return HttpResponse("asd")
def selection_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseSelection/student_selection_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseSelection/teacher_selection_manage.html')
    else:
        return render(request, 'courseSelection/adm_selection_manage.html')
def stu_tongshi(request):
    return render(request,"courseSelection/stu_tongshi.html")

def stu_major(request):
    majorC = Teacher_Schedule_result.objects.all()[:3]
    data=[]
    dat = []
    haveChosen={}

    #     # crno = models.CharField(max_length=128)
    #     # crtype = models.CharField(null=False, max_length=10)
    #     # contain_num = models.IntegerField()
    sno = request.session["username"]
    courseChosen = CourseSelected.objects.filter(sno__username=sno)
    for c in courseChosen:
        tmp = {}
        haveChosen[c.cno.id]=1
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
                tmp["if_chosen"]=1
        except:
            tmp["if_chosen"]=0
        tmp["id"]=major.id
        tmp["课程号"] = major.tno.mcno.cno.cno
        tmp["课程名"] = major.tno.mcno.cno.cname
        tmp["学时"] = major.tno.mcno.hour_total
        tmp["选课人数"] = major.current_number
        tmp["课程容量"] = major.MAX_number
        tmp["授课教师"] = major.tno.tno.name
        tmp["上课教室"] = major.where.crno
        tmp["上课时间"] = major.time
        if tmp["选课人数"] <tmp["课程容量"]:
            data.append(tmp)
    return render(request,"courseSelection/stu_major.html",{'data': json.dumps(data),'dat':json.dumps(dat)})
def select_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            print("asdasd")
            flag = 1
            ID = request.GET.get("id")
            sno = request.session["username"]
            X = np.zeros((25,8,14),dtype=np.int)
            confilict_candidate = CourseSelected.objects.filter(sno__username=sno)#选的不同的课
            tot = 0
            course_time=[]#收集这些课程的上课时间
            for i in confilict_candidate:
                tmp = i.cno.time.split(",")#同一门课程在一周内不同的时间上
                for j in tmp:#一周内不同的天
                    dic = {}
                    district = j.split("-")
                    dic["周数"] = district[2]+"-"+district[3]
                    dic["节次"] = district[0]+"-"+district[1]
                    course_time.append(dic)
            for i in course_time:
                week = i["周数"].split("-")
                times = i["节次"].split("-")
                cstart = 0
                cend = 0
                Day = 0
                if int(times[1])>=1 and int(times[1])<=13:
                    Day = 1
                elif int(times[1])>=14 and int(times[1])<=26:
                    Day = 2
                elif int(times[1])>=27 and int(times[1])<=39:
                    Day = 3
                elif int(times[1])>=40 and int(times[1])<=52:
                    Day = 4
                elif int(times[1])>=53 and int(times[1])<=65:
                    Day = 5
                elif int(times[1])>=66 and int(times[1])<=78:
                    Day = 6
                elif int(times[1])>=79 and int(times[1])<=91:
                    Day = 7

                cstart = int(times[0]) % 13
                cend = int(times[1]) % 13

                if cstart ==0 :
                    cstart = 13
                if cend == 0:
                    cend = 13
                X[int(week[0]):int(week[1])+1,Day,cstart:cend+1] = 1


            stu_new = Student.objects.get(username = sno)
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
                    dic["周数"] = district[2]+"-"+district[3]
                    dic["节次"] = district[0]+"-"+district[1]
                    single_course.append(dic)

                for j in single_course:
                    week = j["周数"].split("-")
                    times = j["节次"].split("-")
                    cstart = 0
                    cend = 0
                    Day = 0
                    if int(times[1])>=1 and int(times[1])<=13:
                        Day = 1
                    elif int(times[1])>=14 and int(times[1])<=26:
                        Day = 2
                    elif int(times[1])>=27 and int(times[1])<=39:
                        Day = 3
                    elif int(times[1])>=40 and int(times[1])<=52:
                        Day = 4
                    elif int(times[1])>=53 and int(times[1])<=65:
                        Day = 5
                    elif int(times[1])>=66 and int(times[1])<=78:
                        Day = 6
                    elif int(times[1])>=79 and int(times[1])<=91:
                        Day = 7

                    cstart = int(times[0]) % 13
                    cend = int(times[1]) % 13
                    if cstart ==0 :
                        cstart = 13
                    if cend == 0:
                        cend = 13
                    
                    if np.sum(X[int(week[0]):int(week[1])+1,Day,cstart:cend+1]) != 0:
                        flag = 0
                        print(flag)
                        break


                if(flag):
                    new_cord = CourseSelected()
                    new_cord.sno = stu_new
                    new_cord.cno = teach
                    new_cord.score=0
                    new_cord.save()
                    tot = teach.current_number
                    tot+=1
                    Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)

                return JsonResponse(
                    {"flag":flag,"tot":tot})
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
            X = CourseSelected.objects.filter(sno__username=sno , cno_id=ID)
            X.delete()

            return JsonResponse({"flag":1,"tot":tot,"ID":ID})

def teacher(request):#教师查看授课选课情况
    return render(request,"courseSelection/index.html")
def find_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            sno = request.session["username"]
            theCourse = CourseSelected.objects.filter(sno__username=sno)

            course_time=[]#收集这些课程的上课时间
            dic = {}
            tmp = {}
            t_info = {}
            t_place = {}
            for i in theCourse:#每门课
                tmp = i.cno.time.split(",")#同一门课程在一周内不同的时间上
                t_info[i.cno.tno.mcno.cno.cname] = i.cno.tno.tno.name
                t_place[i.cno.tno.mcno.cno.cname] = i.cno.where.crno
                dic[i.cno.tno.mcno.cno.cname]=[]
                for j in tmp:#一周内不同的天
                    tp = {}
                    district = j.split("-")
                    tp["周数"] = district[2]+"-"+district[3]
                    tp["节次"] = district[0]+"-"+district[1]
                    dic[i.cno.tno.mcno.cno.cname].append(tp)
            return JsonResponse({"dic":dic,"t_info":t_info, "t_place":t_place})