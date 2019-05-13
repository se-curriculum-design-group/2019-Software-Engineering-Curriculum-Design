import os
import re
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan, User
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from django.db.utils import IntegrityError


