from django.db import models
from backstage.models import Teacher, Student, \
    College, MajorPlan, AdmClass, ClassRoom
from courseScheduling.models import MajorCourses, Teaching, Teacher_Schedule_result
from courseSelection.models import CourseSelected


# 课程成绩表
class CourseScore(models.Model):
    # 对应的课程表
    teaching = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    # 总成绩
    score = models.FloatField()
    commen_score = models.FloatField(default=0)
    final_score = models.FloatField(default=0)

    def __str__(self):
        return '-'.join([str(self.sno), str(self.teaching), str(self.score)])

    class Meta:
        db_table = 'course_score'
        unique_together = (
            'teaching',
            'sno'
        )


# 学生评价表
class EvaluationForm(models.Model):
    # 三个对象引用
    student = models.ForeignKey(
        to=Student, on_delete=models.CASCADE, default=None)
    course = models.ForeignKey(
        to=MajorCourses, on_delete=models.CASCADE, default=None)
    teacher = models.ForeignKey(
        to=Teacher, on_delete=models.CASCADE, default=None)

    # 八个评分项（A=100 B=90 C=75 D=60 E=50）
    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)
    item4 = models.IntegerField(default=0)
    item5 = models.IntegerField(default=0)
    item6 = models.IntegerField(default=0)
    item7 = models.IntegerField(default=0)
    item8 = models.IntegerField(default=0)
    # 评语
    description = models.TextField(default="无")
    # 总分，在前端算完返回给后台
    sum = models.FloatField(default=0)
    # 是否已提交
    is_finish = models.BooleanField(default=False)

    def __str__(self):
        return "-".join([self.student.__str__(), self.course.__str__(), self.teacher.__str__(), str(self.sum)])

    class Meta:
        db_table = 'evaluation_form'
