from django.db import models
from backstage.models import Student, Teacher
from scoreManagement.models import Course, MajorCourses


class CourseSelection(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    major_course = models.ForeignKey(to=MajorCourses, on_delete=models.CASCADE)
    score = models.FloatField()
    
    class Meta:
        db_table = 'course_selection'

    pass
