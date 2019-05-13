from django.db import models
from django.db import models
from courseScheduling.models import Teacher_Schedule_result
# Create your models here.

from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom
from scoreManagement.models import Course,MajorCourses,Teaching


class CourseSelected(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    score = models.FloatField()
    common_score = models.FloatField(null=True)
    final_score = models.FloatField(null=True)
    is_finished = models.BooleanField(null=True)
    class Meta:
        db_table = "course_selected"

