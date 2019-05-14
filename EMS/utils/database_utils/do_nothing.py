import os
import re
import pandas as pd
from random import choice, randint, choices

from django.db.utils import IntegrityError
from django.http import request
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan, User
from courseScheduling.models import Teacher_Schedule_result, MajorCourses, Teaching, Schedule_result
from courseSelection.models import CourseSelected
from scoreManagement.models import EvaluationForm, CourseScore




