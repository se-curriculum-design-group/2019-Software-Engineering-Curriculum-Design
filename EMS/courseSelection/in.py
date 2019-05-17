from django.shortcuts import render, redirect
from django.http import HttpResponse

from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from scoreManagement.models import Course, MajorPlan, MajorCourses, CourseScore,Teaching

from . import models
if __name__ == '__main__':
   teaching_course = Teaching.objects.all()
   print(teaching_course)