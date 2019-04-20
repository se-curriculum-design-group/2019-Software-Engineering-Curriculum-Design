import os
import re
import math
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching
from django.db.utils import IntegrityError


base_dir = '../others/'
xls_file = '2018-2019-1semester.xls'
data_frame = pd.read_excel(os.path.join(base_dir, xls_file))
data_frame = data_frame[data_frame['开课学院'] != '网络']


