from django.shortcuts import render
from courseScheduling.Schedule import *
from django.shortcuts import render
import courseScheduling.Schedule as sch
import backstage.models as mod

def welcome(request):
    exam_schedule()
    return render(request, 'courseScheduing/welcome.html')


def scheduling_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseScheduing/student_scheduling_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseScheduing/teacher_scheduling_manage.html')
    else:
        return render(request, 'courseScheduing/adm_scheduling_manage.html')


def time_exam(request):
    a = [1,2,3,4,5,6]
    b = [1,2,3,4,5,6]
    c = [1,2,3,4,5,6]
    d = [1,2,3,4,5,6]
    e = [1,2,3,4,5,6]
    f = [1,2,3,4,5,6]
    data=[]
    data.append(a)
    data.append(b)
    data.append(c)
    data.append(d)
    data.append(e)
    data.append(f)
    return render(request, "courseScheduing/time_exam.html", {'data':data})

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
    rooms=[]
    sch.init()
    return render(request, 'courseScheduing/student_scheduling_manage.html', {'rooms': rooms})
