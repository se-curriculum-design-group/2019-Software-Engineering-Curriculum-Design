from django.db import models
from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom



#毕设题目表
class GraduationProject(models.Model):
    #题目名称
    pname=models.CharField(max_length=30)
    #教师id
    tno=models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
   
    #题目类型
    pdirection=models.CharField(max_length=10)
    #题目难度
    pdifficulty=models.CharField(max_length=10)
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
    class Meta:
        db_table = 'ProjectDocument'
    # paper=

class ProjectScore(models.Model):
    schoic=models.ForeignKey(to=StuChoice,on_delete=models.CASCADE)
    #答辩成绩
    grade=models.CharField(max_length=2)
    #答辩评语
    comments=models.TextField()
    class Meta:
        db_table = 'ProjectScore'

