from django.db import models
from backstage.models import Student, Teacher
from scoreManagement.models import Teaching, MajorCourses, ClassRoom
from backstage.models import Student, Teacher, ClassRoom


class Schedule_result(models.Model):
    """
        凡是被加在这里的数据，一定是有学生，老师，教室，时间地点已定。
        第一次自动排完后，只有必修课在这里，选修不在，
        选修的同步目前不同步更新
    """
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    def __str__(self):
        return "-".join([self.sno, self.tno, self.where, self.time, ])
    class Meta:
        db_table = 'Schedule_result'
        unique_together = (
            'sno', 'tno', 'where', 'time'
        )


class Teacher_Schedule_result(models.Model):
    tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    current_number = models.IntegerField()
    MAX_number = models.IntegerField()
    state = models.CharField(max_length=128)

    def __str__(self):
        return "-".join([str(self.tno),str(self.where),str(self.crtype),str(self.contain_num),str(self.time),
                         str(self.current_number),str(self.MAX_number),str(self.state)])
    class Meta:
        db_table = 'Teacher_Schedule_result'
        unique_together = (
              'tno', 'where', 'time'
        )

class Classroom_other_schedule (models.Model):
    #外键教室
    crno = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    #时间定义同上
    time = models.CharField(max_length=128, default='')
    statement = models.CharField(max_length=128, default='')
    def __str__(self):
        return "-".join([self.crno, self.time, self.statement])
    class Meta:
        db_table = 'Classroom_other_schedule'

class Exam_Schedule(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    tno_mno_course = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    def __str__(self):
        return "-".join([self.sno, self.tno_mno, self.time, self.where])
    class Meta:
        db_table = 'Exam_Schedule'
        unique_together = (
            'sno', 'tno_mno_course',
        )
