from scoreManagement.models import MajorCourses
from courseScheduling.models import Teacher_Schedule_result, Schedule_result
def change_course_time():
    course = MajorCourses.objects.all()
    for element in course:
        score_time = element.cno.score
        if score_time < 10.0:
            time = int(score_time*16)
            if time != element.hour_total or time != element.hour_class:
                element.hour_total = time
                element.hour_class = time
                element.save()
def delete():
    row = Teacher_Schedule_result.objects.all()
    for e in row:
        e.delete()
    row = Schedule_result.objects.all()
    for e in row:
        e.delete()

if __name__ == '__main__':
    change_course_time()
    delete()