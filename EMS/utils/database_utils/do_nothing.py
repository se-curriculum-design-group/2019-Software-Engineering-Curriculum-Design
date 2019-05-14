import os
import re
import pandas as pd
from random import choice, randint, choices

from django.db.utils import IntegrityError
from django.http import request
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan, User
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from courseScheduling.models import Teacher_Schedule_result
from courseSelection.models import CourseSelected




