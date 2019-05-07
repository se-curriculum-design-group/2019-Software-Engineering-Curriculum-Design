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

"""
class Teacher_Schedule_result(models.Model):
    tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    current_number = models.IntegerField()
    MAX_number = models.IntegerField()
    state = models.CharField(max_length=128)

    def __str__(self):
        return "-".join([self.tno, self.where, self.time, ])
    class Meta:
        db_table = 'Teacher_Schedule_result'
        unique_together = (
              'tno', 'where', 'time'
        )
"""
