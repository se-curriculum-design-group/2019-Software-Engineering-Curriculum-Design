from scoreManagement.models import Teaching, CourseScore


for cs in CourseScore.objects.all():
    w = cs.teaching.weight
    cs.commen_score = 0
    cs.final_score = 0
    cs.commen_score = round(cs.score / (1-w), 2)
    cs.final_score = round(cs.score / w, 2)
    cs.save()
