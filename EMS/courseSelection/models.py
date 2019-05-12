from django.db import models
from django.db import models
from courseScheduling.models import Teacher_Schedule_result
# Create your models here.

from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom
from scoreManagement.models import Course,MajorCourses,Teaching


class courseSelected(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        db_table = "courseSelected"

