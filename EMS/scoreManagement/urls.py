from django.urls import path, include

from django.conf.urls import url
from . import views

app_name = 'scoreManagement'
urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('score_home_page', views.score_home_page, name="score_home_page"),
    # 学生查看自己的成绩
    path('student_view_score', views.student_view_score, name="student_view_score"),
    # 学生查看个人学业情况
    path('student_own_study', views.student_own_study, name="student_own_study"),
    # 各个角色查看专业计划和课程计划
    path('std_view_major_course', views.std_view_major_course,
         name="std_view_major_course"),
    path('std_view_major_plan', views.std_view_major_plan,
         name="std_view_major_plan"),
    path('teacher_view_major_course', views.teacher_view_major_course,
         name="teacher_view_major_course"),
    path('teacher_view_major_plan', views.teacher_view_major_plan,
         name="teacher_view_major_plan"),
    path('adm_view_major_course', views.adm_view_major_course,
         name="adm_view_major_course"),
    path('adm_view_major_plan', views.adm_view_major_plan,
         name="adm_view_major_plan"),

    # 学生评价教师
    path('assess_teacher', views.assess_teacher, name="assess_teacher"),
    # 学生提交评教结果
    path('submit_result', views.submit_result, name="submit_result"),
    path('submit_all', views.submit_all, name="submit_all"),

    # 教师查看自己教的课
    path('teacher_view_teaching', views.teacher_view_teaching, name="teacher_view_teaching"),
    # 教师上传成绩
    path('teacher_upload_score', views.teacher_upload_score, name="teacher_upload_score"),
    # 教师上传成绩--查看并选择要上传的课程
    path('get_all_course_selected', views.get_all_course_selected, name="get_all_course_selected"),
    # 教师查看学生考试成绩
    path('teacher_view_stu_score', views.teacher_view_stu_score, name="teacher_view_stu_score"),
    # 教师进入到详细的上分页面，下载模板上分等
    path('upload_student_score/?cno=<cno>&course_type=<course_type>', views.upload_student_score, name="upload_student_score"),

    # 管理员查看全部的成绩
    path('adm_all_course_score', views.adm_all_course_score,
         name="adm_all_course_score"),

    # 管理员想查看成绩，先查看自己教的课
    path('get_all_teaching', views.get_all_teaching, name="get_all_teaching"),
    # 管理员进入页面，查看学生成绩详情
    path('show_student_score/?cno=<cno>&course_type=<course_type>', views.show_student_score, name="show_student_score"),

    # 管理员查看教学评价结果
    path('adm_view_teacher_evaluation', views.adm_view_teacher_evaluation, name="adm_view_teacher_evaluation"),

    # 管理员修改成绩
    path('adm_change_score', views.adm_change_score, name="adm_change_score"),
    # 管理员修改专业计划
    path('adm_change_major_plan', views.adm_change_major_plan, name="adm_change_major_plan"),
    # 管理员修改专业课程信息
    path('adm_change_major_course', views.adm_change_major_course, name="adm_change_major_course"),
    # 管理员添加专业课程信息
    path('adm_add_major_course', views.adm_add_major_course, name="adm_add_major_course"),
    # 管理员删除专业课程信息
    path('adm_delete_major_course', views.adm_delete_major_course, name="adm_delete_major_course"),

    # 管理员修改Course
    path('adm_change_course', views.adm_change_course, name="adm_change_course"),
    # 管理员添加Course
    path('adm_add_course', views.adm_add_course, name="adm_add_course"),
    # 管理员删除Course
    path('adm_delete_course', views.adm_delete_course, name="adm_delete_course"),
]
