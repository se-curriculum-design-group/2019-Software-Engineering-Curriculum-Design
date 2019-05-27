from courseSelection.models import CourseSelected as courseSelected
from courseScheduling.models import Schedule_result, Teacher_Schedule_result

def Sychronize_with_courseSelected(year=2019, semester=2):
    rows_in_Schedule_result = Schedule_result.objects.filter(tno__mcno__year=year, tno__mcno__semester=semester)
    for element in rows_in_Schedule_result:
        if len(courseSelected.objects.filter(
                cno__where=element.where,
                cno__time=element.time,
                cno__tno=element.tno,
                sno=element.sno,
        )) == 0:
            Tsr = Teacher_Schedule_result.objects.get(tno=element.tno, where=element.where, time=element.time)
            courseSelected.objects.create(sno=element.sno, cno=Tsr, score=0, common_score=0, final_score=0,
                                          is_finish=False).save()


if __name__ == '__main__':
    Sychronize_with_courseSelected()
