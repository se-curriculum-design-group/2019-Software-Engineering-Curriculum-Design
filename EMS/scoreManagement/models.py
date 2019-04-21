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
    tno = models.ManyToManyField(to=Teacher)
    # 教授课程的教师名称，为了显示方便，可以冗余
    # tname = tno.username
    # 这门课对应所在的专业培养计划
    mcno = models.ManyToManyField(to=MajorCourses)
    # 教师给的本课程的平时分权重，如：0.3, 0.2 ...
    weight = models.FloatField()

    def __str__(self):
        return '-'.join([str(self.tno), str(self.mcno)])

    class Meta:
        db_table = 'teaching_table'


class CourseScore(models.Model):
    # 对应的课程表
    teaching = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    # 总成绩
    score = models.FloatField()

    def __str__(self):
        return '-'.join([str(self.sno), str(self.teaching), str(self.score)])

    class Meta:
        db_table = 'course_score'
        unique_together = (
            'teaching',
            'sno'
        )


class EvaluationForm(models.Model):
    teaching = models.OneToOneField(to=Teaching, on_delete=models.CASCADE)
    item1 = models.CharField(max_length=128)
    item2 = models.CharField(max_length=128)
    item3 = models.CharField(max_length=128)
    item4 = models.CharField(max_length=128)
    item5 = models.CharField(max_length=128)
    item6 = models.CharField(max_length=128)
    description = models.TextField()
    is_finish = models.BooleanField()

    def __str__(self):
        return str(self.teaching)

    class Meta:
        db_table = 'evaluation_form'

