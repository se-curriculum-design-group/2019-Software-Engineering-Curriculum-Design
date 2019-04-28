import os
import re
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student, \
    Teacher, ClassRoom, MajorPlan, User
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from django.db.utils import IntegrityError


def change_score():
    for course_score in CourseScore.objects.all():
        course_score.commen_score = course_score.score * (1 - course_score.teaching.weight)
        course_score.final_score = course_score.score * course_score.teaching.weight
        course_score.save()

change_score()
