from django.db import models
from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom

#题目方向表:理论研究，设计应用
class ProjectDirection(models.Model):
	pdiname=models.CharField(max_length=10)
#题目难度表
class ProjectDifficulty(models.Model):
    pdname=models.CharField(max_length=10)

#毕设题目表
class GraduationProject(models.Model):
    #题目名称
    pname=models.CharField(max_length=30)
    #教师id
    tno=models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    # #题目类型
    # ptype=models.ForeignKey(to=ProjectType,on_delete=models.CASCADE)
    #题目方向
    pdirection=models.ForeignKey(to=ProjectDirection,on_delete=models.CASCADE)
    #题目难度
    pdifficulty=models.ForeignKey(to=ProjectDifficulty,on_delete=models.CASCADE)
    #题目关键词
    pkeywords=models.TextField()
    #题目详细描述
    pdescription=models.TextField()
    #题目对学生的要求
    pstu=models.TextField()
    #题目状态
    pstatus=models.IntegerField(default=0)

    class Meta:
        db_table = 'GraduationProject'

#学生选题表
class StuChoice(models.Model):
	#学生编号
    sno=models.ForeignKey(to=Student,on_delete=models.CASCADE)
    #教师编号
    tno=models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    #课题编号
    pno=models.ForeignKey(to=GraduationProject,on_delete=models.CASCADE)
    #学生状态
    status=models.IntegerField(default=0)

    class Meta:
        db_table = 'StuChoice'
        unique_together = (
            'sno', 'tno', 'pno'
        )

class ProjectDocument(models.Model):
	schoic=models.ForeignKey(to=StuChoice,on_delete=models.CASCADE)
    # paper=

class ProjectScore(models.Model):
    schoic=models.ForeignKey(to=StuChoice,on_delete=models.CASCADE)
    #答辩成绩
    grade=models.CharField(max_length=2)
    #答辩评语
    comments=models.TextField()

