from django.db import models
from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom


# 课程信息
class Course(models.Model):
    # 课程编号，长度必须为9位，如：MAT13904T--高数
    # 3位英文+5位数字+一位英文
    cno = models.CharField(max_length=9)
    # 课程名称，需要与编号对应
    cname = models.CharField(max_length=128)
    # 开课学院，需要从学院中选取对应的老师来上课
    college = models.ForeignKey(to=College, on_delete=models.CASCADE)
    # 课程性质
    course_type = models.CharField(max_length=128, null=True)
    # 该门课程在该专业对应的学分
    score = models.FloatField()

    def __str__(self):
        return "-".join([self.cno, self.cname, self.course_type])

    class Meta:
        db_table = 'course'
        unique_together = (
            'cno',
            'cname',
            'course_type'
        )


# 专业对应课程信息
class MajorCourses(models.Model):
    # 课程编号
    cno = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    # cname = cno.cname
    # 对应到的专业计划信息
    # 注意，这里都是外键，需要传入的是对象引用
    mno = models.ForeignKey(to=MajorPlan, on_delete=models.CASCADE)
    # 该门课程在该专业对应的总学时
    hour_total = models.IntegerField()
    # 讲课学时，总学时中用于讲课的学时
    hour_class = models.IntegerField()
    # 实践学时, hour_total - hour_class
    hour_other = models.IntegerField()
    # 开课学年，主要这里的开课学年与MajorPlan中的年级不同
    # 这里是指上这门课的学年
    year = models.IntegerField()
    # 开课学期1, 2, 3学期，3表示小学期
    semester = models.IntegerField()
    # 考核方式，考核--True or 考察--False
    exam_method = models.BooleanField(default=True)

    def __str__(self):
        return "-".join([self.cno.__str__(), self.mno.__str__(), str(self.year), str(self.semester)])

    class Meta:
        # 设置数据库中表的显示名称
        db_table = 'major_courses'
        # 设置数据联合主键，为全码
        unique_together = (
            'cno', 'mno', 'year', 'semester'
        )


# 教师授课
class Teaching(models.Model):
    # 教授课程的教师工号
    tno = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, default=None)
    # 教授课程的教师名称，为了显示方便，可以冗余
    # tname = tno.username
    # 这门课对应所在的专业培养计划
    mcno = models.ForeignKey(
        to=MajorCourses, on_delete=models.CASCADE, default=None)
    # 教师给的本课程的平时分权重，如：0.3, 0.2 ...
    weight = models.FloatField()

    def __str__(self):
        return '-'.join([str(self.tno), str(self.mcno)])

    class Meta:
        db_table = 'teaching_table'
        unique_together = (
            'tno',
            'mcno'
        )


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
