from django.db.models import Avg, Sum, Max, Min
import numpy as np

from backstage.models import Student, Major, MajorPlan, Teacher
from .models import CourseScore, MajorCourses, Teacher, Teaching


def stu_search_course(student, year, semester):
    """
    学生查看自己本学期的成绩，包括了考试总分和平时分等成绩明细
    :param student: 传入学生实例或学号id
    :return:QuerySet
    """
    if isinstance(student, Student):
        return CourseScore.objects.filter(sno=student)
    elif isinstance(student, str):
        try:
            student = Student.objects.get(username=student)
            return CourseScore.objects.filter(sno=student)
        except Student.DoesNotExist:
            print("Student username error!")


def teacher_search_course(teacher):
    """
    :param teacher:
    :return: QuerySet。老师所教的课程集合
    """
    if isinstance(teacher, Teacher):
        return Teaching.objects.filter(tno=teacher)
    elif isinstance(teacher, str):
        try:
            teacher = Teacher.objects.get(username=teacher)
            return Teaching.objects.filter(tno=teacher)
        except Teacher.DoesNotExist:
            print("Teacher username error!")


def stu_view_stat(student):
    """获取到学生成绩的统计信息"""
    stu_course = stu_search_course(student)
    scores = []
    for course in stu_course:
        scores.append(course.score)
    scores = np.array(scores)
    return {
        'mean': scores.mean(),
        'max': scores.max(),
        'mode': np.argmax(np.bincount(np.int(scores))),
        'median': np.median(scores)
    }


def stu_proposal():
    raise NotImplementedError


def stu_print_score():
    raise NotImplementedError


def stu_comment_tch():
    raise NotImplementedError


def tch_upload_score_xls():
    raise NotImplementedError


def tch_upload_score_online():
    raise NotImplementedError


def tch_print_score():
    raise NotImplementedError


def tch_download_score():
    raise NotImplementedError


def tch_proposal():
    raise NotImplementedError


def get_xls_template():
    raise NotImplementedError


def mg_view_proposal():
    raise NotImplementedError


def get_xls_to_instructor():
    raise NotImplementedError


def cal_stu_gpa(student):
    raise NotImplementedError


def cal_total_gpa():
    raise NotImplementedError


def get_stu_course_score():
    raise NotImplementedError


def get_class_mean():
    raise NotImplementedError


def get_class_max():
    raise NotImplementedError


def get_class_excelent():
    raise NotImplementedError


def get_class_excelent_rat():
    raise NotImplementedError


def get_major_gpa_mean():
    raise NotImplementedError


def get_major_gpa_max():
    raise NotImplementedError


def get_major_gpa_mode():
    raise NotImplementedError


def get_major_failed():
    raise NotImplementedError


def get_major_failed_rat():
    raise NotImplementedError


def get_major_num():
    raise NotImplementedError


def get_class_failed():
    raise NotImplementedError


def get_class_failed_rat():
    raise NotImplementedError


def get_class_num():
    raise NotImplementedError


def get_stu_in_range():
    raise NotImplementedError


def table_to_pdf():
    raise NotImplementedError


def send_annocement():
    raise NotImplementedError
