from django.shortcuts import render
from courseScheduling.Schedule import *
from django.http import JsonResponse
from django.shortcuts import render
import courseScheduling.Schedule as sch
import backstage.models as mod
from . import models

def welcome(request):
    #exam_schedule()
    return render(request, 'courseScheduing/welcome.html')


def scheduling_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseScheduing/student_scheduling_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseScheduing/teacher_scheduling_manage.html')
    else:
        return render(request, 'courseScheduing/adm_scheduling_manage.html')

def get_exam_time(time_class):
    ss = "考试周 星期"
    if time_class[0] == "0":
        ss += "一"
    elif time_class[0] == "1":
        ss += "二"
    elif time_class[0] == "2":
        ss += "三"
    elif time_class[0] == "3":
        ss += "四"
    elif time_class[0] == "4":
        ss += "五"
    elif time_class[0] == "5":
        ss += "六"
    elif time_class[0] == "6":
        ss += "七"
    else:
        pass
    ss += "  "
    if time_class[1] == "0":
        ss += "8.00-10:00"
    elif time_class[1] == "1":
        ss += "10:30-12:30"
    elif time_class[1] == "2":
        ss += "13:00-15:00"
    elif time_class[1] == "3":
        ss += "15:30-17:30"
    elif time_class[1] == "4":
        ss += "18:00-20:00"
    else:
        pass
    return ss

def time_exam(request):
    if request.method == 'POST':
        print("收到输入")
        # 若全为0 则查询所有内容
        year = int(request.POST.get('year'))
        term = int(request.POST.get('term'))
        # print(year, term)
        username = request.session['username']
        # print(username)
        # 以下list为往前端传的list
        year_list = []
        term_list = []
        cname_list = []
        tname_list = []
        time_list = []
        data = []

        exam_schedule = models.Exam_Schedule.objects.filter(sno__username=username)
        if len(exam_schedule)>0:
            print("查询有效")
            for i in exam_schedule:
                f = 0
                exam_message = []
                time_class = i.time.split("-")
                tno_mno_course = i.tno_mno_course
                # print(type(tno_mno_course))
                tno = tno_mno_course.tno
                # print()
                tname = tno.tno.name
                mcno = tno.mcno
                year_class = mcno.year
                term_class = mcno.semester
                cname = mcno.cno.cname
                # print(cname, year_class, term_class)
                if year==0 and term==0:
                    exam_message.append(str(year_class)+"-"+str(year_class+1))
                    exam_message.append(str(term_class))
                    exam_message.append(cname)
                    exam_message.append(tname)
                    ss = get_exam_time(time_class)
                    exam_message.append(ss)
                    f= 1
                elif year==0:
                    if term_class==term:
                        exam_message.append(str(year_class) + "-" + str(year_class + 1))
                        exam_message.append(str(term_class))
                        exam_message.append(cname)
                        exam_message.append(tname)
                        ss = get_exam_time(time_class)
                        exam_message.append(ss)
                        f=1
                    else:
                        pass
                elif term==0:
                    if year_class==year:
                        exam_message.append(str(year_class) + "-" + str(year_class + 1))
                        exam_message.append(str(term_class))
                        exam_message.append(cname)
                        exam_message.append(tname)
                        ss = get_exam_time(time_class)
                        exam_message.append(ss)
                        f=1
                    else:
                        pass
                else:
                    if year_class==year and term_class==term:
                        print("均有选择")
                        exam_message.append(str(year_class) + "-" + str(year_class + 1))
                        exam_message.append(str(term_class))
                        exam_message.append(cname)
                        exam_message.append(tname)
                        ss = get_exam_time(time_class)
                        exam_message.append(ss)
                        f=1
                    else:
                        pass
                if f == 1:
                    data.append(exam_message)

    # exam_schedule = list(exam_schedule)
    # print(type(exam_schedule))
    # print(exam_schedule[0])
    # print(type(exam_schedule[0]))
    # print(exam_schedule[0].time)
    # print(type(exam_schedule[0].time))
        return render(request, "courseScheduing/time_exam.html", {"data":data})
    return render(request, "courseScheduing/time_exam.html")

def find_vacant_room(request):
    rooms = mod.ClassRoom.objects.all()
    # rooms=models.Classroom_other_schedule.objects.all()
    # if rooms is not None:
    #     print(rooms)
    # for r in rooms:
    #     print(r.crtype)
    return render(request, 'courseScheduing/student_scheduling_manage.html', {'rooms': rooms})


def search_time_room(request):
    w = int(request.POST.get('week'))
    d = int(request.POST.get('day'))
    ls = int(request.POST.get('ls'))
    le = int(request.POST.get('le'))
    print(w, d, ls, le)
    t = str((d - 1) * 13 + ls) + "-" + str((d - 1) * 13 + le) + "-" + str(w) + "-" + str(w)
    print(t)
    # rooms=[]
    # sch.init()
    rooms=sch.Search_time_room(t)
    # print(rooms)
    return render(request, 'courseScheduing/student_scheduling_manage.html', {'rooms': rooms})

def search_time_room_teacher(request):
    w = request.POST.get('week')
    d = request.POST.get('day')
    ls = request.POST.get('ls')
    le = request.POST.get('le')
    if w==None or w=='' or d==None or d=='' or ls==None or ls=='' or le==None or le=='':
        rooms=[]
        return render(request, 'courseScheduing/teacher_scheduling_manage.html', {'rooms': rooms})
    w=int(w)
    d=int(d)
    ls=int(ls)
    le=int(le)
    print(w, d, ls, le)
    t = str((d - 1) * 13 + ls) + "-" + str((d - 1) * 13 + le) + "-" + str(w) + "-" + str(w)
    print(t)
    # rooms=[]
    # sch.init()
    rooms=sch.Search_time_room(t)
    # print(rooms)
    return render(request, 'courseScheduing/teacher_scheduling_manage.html', {'rooms': rooms})

w,d,ls,le,note=0,0,0,0,0

def occupy_room(request):
    global w,d,ls,le,note
    w = request.POST.get('week')
    d = request.POST.get('day')
    ls = request.POST.get('ls')
    le = request.POST.get('le')
    # print(week, day, ls, le)
    if w == None or w == '' or d == None or d == '' or ls == None or ls == '' or le == None or le == '':
        rooms=[]

        return render(request, 'courseScheduing/occupy_room.html', {'rooms': rooms})
    w = int(w)
    d = int(d)
    ls = int(ls)
    le = int(le)
    if w == 0 and d == 0 and ls == 0 and le == 0:
        rooms = []
        return render(request, 'courseScheduing/occupy_room.html', {'rooms': rooms})
    print(w, d, ls, le)
    t = str((d - 1) * 13 + ls) + "-" + str((d - 1) * 13 + le) + "-" + str(w) + "-" + str(w)
    print(t)
    print("asdasd")

    ppp = models.ClassRoom.objects.all()
    a = request.POST.get('B-101')
    print(a)
    rooms=[]
    # sch.init()
    rooms = sch.Search_time_room(t)
    # print(rooms)
    return render(request, "courseScheduing/occupy_room.html", {'rooms': rooms})

# def occupy_room(request):
#     global w,d,le,ls,note
#     # print("Asd")
#     if request.is_ajax():
#         # print("第一层")
#         if request.method=='GET':
#             week = request.GET.get('week')
#             day = request.GET.get('day')
#             ls = request.GET.get('ls')
#             le = request.GET.get('le')
#             # print(week, day, ls, le)
#             w = int(week)
#             d = int(day)
#             ls = int(ls)
#             le = int(le)
#             # print(w, d, ls, le)
#             t = str((d - 1) * 13 + ls) + "-" + str((d - 1) * 13 + le) + "-" + str(w) + "-" + str(w)
#             # print(t)
#             # rooms=[]
#             # sch.init()
#             rooms = sch.Search_time_room(t)
#             id={}
#             type = {}
#             container={}
#             co = 0
#             for i in rooms:
#                 # print(i.get('id'), i.get('type'), i.get('container'))
#                 id[co] = i.get('id')
#                 type[co] = i.get('type')
#                 container[co] = i.get('container')
#                 co+=1
#             return JsonResponse({"idd":id, "typee":type, "con":container})
#
#     # print(w,d,ls,le,note)
#     if w==None or w=='' or d==None or d=='' or ls==None or ls=='' or le==None or le=='':
#         rooms=[]
#         return render(request, 'courseScheduing/occupy_room.html', {'rooms': rooms})
#     we=str(w)
#     sta = (d-1)*13+ls
#     end = (d-1)*13+le
#     sss = we+"-"+we+"-"+str(sta)+"-"+str(end)
#     ppp = models.ClassRoom.objects.all()
#     for i in ppp:
#         if request.GET.get(i):
#             print('asd')
#             print(i)
#     # sch.add_active(sss,)
#     # print(rooms)
#     return render(request, 'courseScheduing/occupy_room.html')


def schedule(request):
    s=request.POST.get("s")
    t=request.POST.get('t')
    ws=request.POST.get("ws")
    we=request.POST.get("we")
    d1=request.POST.get("d1")
    f1=request.POST.get("f1")
    e1=request.POST.get("e1")
    d2=request.POST.get("d2")
    f2=request.POST.get("f2")
    e2=request.POST.get("e2")
    cd=request.POST.get('cd')
    r=request.POST.get('rooms')
    print(r,s,t,cd,d1,f1,e1)
    if r is None or s is None or t is None or cd is None or e1 is None or d1 is None or f1 is None or\
                (len(r) and len(s) and len(t) and len(e1) and len(cd) and len(d1) and len(f1)) == 0:
        return render(request,"courseScheduing/schedule.html",{'f':0})
    time1 = str((int(d1) - 1) * 13 + int(f1)) + "-" + str((int(d1) - 1) * 13 + int(e1)) + "-" + ws + "-" + we
    time2 = ""
    if len(d2) == 0 or len(f2) == 0 or len(e2) == 0:
        time2 = ""
    else:
        time2 = ',' + str((int(d2) - 1) * 13 + int(f2)) + "-" + str((int(d2) - 1) * 13 + int(e2)) + "-" + ws + "-" + we

    time3=time1+time2

    f=manual_schedule(time3, r, str(s).split(' '), [], t,cd)

    if f==True:
        return render(request,'courseScheduing/schedule.html',{"f":1})
    else:
        return render(request, 'courseScheduing/schedule.html', {"f": 2})


