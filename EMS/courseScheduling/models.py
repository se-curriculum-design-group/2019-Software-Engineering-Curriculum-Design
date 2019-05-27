from django.db import models
from backstage.models import Student, Teacher, ClassRoom, College, AdmClass, Major, MajorPlan


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
        db_table = 'schedule_result'
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
        return "-".join([str(self.tno), str(self.where), str(self.time),
                         str(self.current_number), str(self.MAX_number), str(self.state)])
    class Meta:
        db_table = 'teacher_schedule_result'
        unique_together = (
            'tno', 'where', 'time'
        )


class Classroom_other_schedule(models.Model):
    # 外键教室
    crno = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    # 时间定义同上
    time = models.CharField(max_length=128, default='')
    statement = models.CharField(max_length=128, default='')

    def __str__(self):
        return "-".join([self.crno, self.time, self.statement])

    class Meta:
        db_table = 'classroom_other_schedule'


class Exam_Schedule(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    tno_mno_course = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return "-".join([self.sno.username, self.tno_mno_course.tno.mcno.cno.cname, self.time, self.where.crno])

    def get_class_name(self):
        return self.tno_mno_course.tno.mcno.cno.cname

    class Meta:
        db_table = 'exam_schedule'
        unique_together = (
            'sno', 'tno_mno_course',
        )
