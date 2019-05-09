from django.db import models
from django.db import models
from courseScheduling.models import Teacher_Schedule_result
# Create your models here.

from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom
from scoreManagement.models import Course,MajorCourses,Teaching


# class Teacher_Schedule_result(models.Model):
#     tno = models.ForeignKey(to=Teaching,on_delete=models.CASCADE)
#     where = models.ForeignKey(to=ClassRoom,on_delete=models.CASCADE)
#     # crno = models.CharField(max_length=128)
#     # crtype = models.CharField(null=False, max_length=10)
#     # contain_num = models.IntegerField()
#     time = models.CharField(max_length=128,null=False)
#     current_number = models.IntegerField()
#     MAX_number = models.IntegerField()
#     state = models.CharField(max_length=128)
#     # hhhhs
#
#     def __str__(self):
#         return "-".join([str(self.tno),str(self.crno),str(self.crtype),str(self.contain_num),str(self.time),
#                          str(self.current_number),str(self.MAX_number),str(self.state)])
#     class Meta:
#         db_table = 'Teacher_Schedule_result'
#         unique_together=(
#             'tno','time'
#         )


class courseSelected(models.Model):
    sno = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Teacher_Schedule_result,on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        db_table = "courseSelected"

# class TeachersCourse(models.Model):
#     tno = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
#     course = models.ForeignKey(to=MajorCourses,on_delete=models.CASCADE)
#     stu_num = models.IntegerField()

'''class Teacher_Schedule_result(models.Model):
    tno = models.ForeignKey(to=Teaching,on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom,on_delete=models.CASCADE)
    # crno = models.CharField(max_length=128)
    # 教室类型，阶教180人，中等教室120人，小教室50人
    # 教室类型需要和教室编号对应
    # crtype = models.CharField(null=False, max_length=10)

    # 教室能够容纳的学生数目，需要与类型对应
    # contain_num = models.IntegerField()

    time = models.CharField(max_length=128,null=False)
    current_number = models.IntegerField()
    MAX_number = models.IntegerField()
    state=models.CharField(max_length=128)
    def __str__(self):
        return "-".join([self.tno,self.time,])
    class Meta:
        db_table = 'Teacher_Schedule_result'
        unique_together = (
            'tno','time'
        )'''

'''class course_for_select(models.Model):
    tno = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom,on_delete=models.CASCADE)
    cno = models.ForeignKey(to=MajorCourses,on_delete=models.CASCADE)

    crno = models.CharField(max_length=128)
    # 教室类型，阶教180人，中等教室120人，小教室50人
    # 教室类型需要和教室编号对应
    crtype = models.CharField(null=False, max_length=10)

    # 教室能够容纳的学生数目，需要与类型对应
    contain_num = models.IntegerField()

    time = models.CharField(max_length=128,null=False)
    current_number = models.IntegerField()
    MAX_number = models.IntegerField()
    state=models.CharField(max_length=128)
    def __str__(self):
        return "-".join([self.tno,self.time,])
    class Meta:
        db_table = 'Teacher_Schedule_result'
        unique_together = (
            'tno','time'
        )'''
# class Schedule_result(models.Model):
#     """
#         凡是被加在这里的数据，一定是有学生，老师，教室，时间地点已定。
#         第一次自动排完后，只有必修课在这里，选修不在，
#         选修的同步目前不同步更新
#     """
#     sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
#     tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
#     where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
#     time = models.CharField(max_length=128, null=False)
#     def __str__(self):
#         return "-".join([self.sno, self.tno, self.where, self.time, ])
#     class Meta:
#         db_table = 'Schedule_result'
#         unique_together = (
#             'sno', 'tno', 'where', 'time'
#         )


# class Teacher_Schedule_result(models.Model):
#     """
#     """
#     tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
#     where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
#     time = models.CharField(max_length=128, null=False)
#     current_number = models.IntegerField()
#     MAX_number = models.IntegerField()
#     state = models.CharField(max_length=128)
#
#     def __str__(self):
#         return "-".join([self.tno, self.where, self.time, ])
#     class Meta:
#         db_table = 'Teacher_Schedule_result'
#         unique_together = (
#               'tno', 'where', 'time'
#         )











