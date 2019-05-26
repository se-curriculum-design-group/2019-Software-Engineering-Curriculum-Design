import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMS.settings')
django.setup()

import re
import pandas as pd
from random import choice, randint, choices

from django.db.utils import IntegrityError
from django.http import request
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan, User
from courseScheduling.models import Teacher_Schedule_result, MajorCourses, Teaching, Schedule_result, Course
from courseSelection.models import CourseSelected
from scoreManagement.models import EvaluationForm, CourseScore

from django.db.models import Count, Avg, Sum, StdDev




