from django.db import models
from django.db import models
from courseScheduling.models import Teacher_Schedule_result
from backstage.models import Teacher, Student, \
    College, MajorPlan, AdmClass, ClassRoom


class CourseSelected(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    score = models.FloatField()
    common_score = models.FloatField(default=0)
    final_score = models.FloatField(default=0)
    is_finish = models.BooleanField(default=False)

    def __str__(self):
        return '-'.join([str(self.sno), str(self.cno), str(self.is_finish)])

    class Meta:
        db_table = "course_selected"
