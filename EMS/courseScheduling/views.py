from django.shortcuts import render
from courseScheduling.Schedule import *
from django.shortcuts import render
import courseScheduling.Schedule as sch
import backstage.models as mod

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
