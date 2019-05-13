from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'graduationManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  #首页
                  path('graduation_home_page', views.graduation_home_page, name="graduation_home_page"),
                  #学生查看选题列表并选题
                  path('student_choose_project',views.student_choose_project,name="student_choose_project"),
                  #学生提交资料
                  path('student_submit_project',views.student_submit_project,name="student_submit_project"),
                  #学生查看资料
                  path('student_view_project',views.student_submit_project,name="student_submit_project"),
                  #学生查看成绩
                  path('student_view_score',views.student_view_score,name="student_view_score"),
                  #学生查看选题详情
                  path('student_view_project_detail',views.student_view_project_detail,name="student_view_project_detail"),
                  #学生查看审核结果
                  path('student_view_project_ischoosen',views.student_view_project_ischoosen,name="student_view_project_ischoosen"),
                  #学生查看审核结果详情
                  path('student_view_project_ischoosendetail',views.student_view_project_ischoosendetail,name="student_view_project_ischoosendetail"),                 
                  #教师提交选题
                  path('teacher_edit_project',views.teacher_edit_project,name="teacher_edit_project"),
                  #教师查看选题
                  path('teacher_submit_project',views.teacher_submit_project,name="teacher_submit_project"),                
                  #教师审核学生
                  path('teacher_choose_student',views.teacher_choose_student,name="teacher_choose_student"),
                  #教师查看资料
                  path('teacher_view_projectfiles',views.teacher_view_projectfiles,name="teacher_view_projectfiles"),
                  #教师查看资料详情
                  path('teacher_view_projectfiles_detail',views.teacher_view_projectfiles_detail,name="teacher_view_projectfiles_detail"),
                  #教师提交成绩
                  path('teacher_submit_score',views.teacher_submit_score,name="teacher_submit_score"),                
                  #教师提交成绩
                  path('teacher_submit_score_detail',views.teacher_submit_score_detail,name="teacher_submit_score_detail"),                
                  #教师查看题目详情
                  path('teacher_view_project_detail',views.teacher_view_project_detail,name="teacher_view_project_detail"),                
                                    
              ]
