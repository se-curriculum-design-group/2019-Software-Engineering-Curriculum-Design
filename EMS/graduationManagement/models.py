from django.db import models
from backstage.models import Teacher, Student, \
    College, MajorPlan, AdmClass, ClassRoom


# 毕设题目表
class GraduationProject(models.Model):
    # 题目名称
    pname = models.CharField(max_length=30)
    # 教师id
    tno = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)

    # 题目类型
    pdirection = models.CharField(max_length=10)
    # 题目难度
    pdifficulty = models.CharField(max_length=10)
    # 题目关键词
    pkeywords = models.TextField()
    # 题目详细描述
    pdescription = models.TextField()
    # 题目对学生的要求
    pstu = models.TextField()
    # 题目状态
    pstatus = models.IntegerField(default=0)

    class Meta:
        db_table = 'graduationproject'


# 学生选题表
class StuChoice(models.Model):
    # 学生编号
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    # 教师编号
    tno = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    # 课题编号
    pno = models.ForeignKey(to=GraduationProject, on_delete=models.CASCADE)
    # 学生状态
    status = models.IntegerField(default=0)  # 2拒绝  1被接受  0未审核

    class Meta:
        db_table = 'stuchoice'
        unique_together = (
            'sno', 'tno', 'pno'
        )


class ProjectDocument(models.Model):
    schoic = models.ForeignKey(to=StuChoice, on_delete=models.CASCADE)
    # 中期报告，最终报告
    dtype = models.CharField(max_length=10)
    dpath = models.TextField()

    class Meta:
        db_table = 'projectdocument'
    # paper=


class ProjectScore(models.Model):
    project = models.ForeignKey(to=ProjectDocument, on_delete=models.CASCADE)
    # 答辩成绩
    # 论述是否充分合理  30%
    lundian = models.IntegerField(default=0)
    # 设计方案是否深入  40%
    fangan = models.IntegerField(default=0)
    # 问题回答情况 30%
    dabian = models.IntegerField(default=0)
    # 中期报告/最终报告分数
    grade = models.IntegerField(default=0)
    # 答辩评语
    comments = models.TextField()

    class Meta:
        db_table = 'projectscore'


class FinalProjectScore(models.Model):
    project = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    # 中期*40%+最终*60%
    grade = models.IntegerField(default=0)

    class Meta:
        db_table = 'finalprojectscore'
