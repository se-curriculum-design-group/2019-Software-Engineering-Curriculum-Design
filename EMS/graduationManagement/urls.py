from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'graduationManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  #首页
                  path('graduation_home_page', views.graduation_home_page, name="graduation_home_page"),
                  path('student_delete',views.student_delete,name="student_delete"),
                  path('student_choosing_action',views.student_choosing_action,name="student_choosing_action"),
                  #学生查看选题列表并选题
                  path('student_choose_project',views.student_choose_project,name="student_choose_project"),
                  #学生提交资料
                  path('student_submit_project',views.student_submit_project,name="student_submit_project"),
                  #学生查看资料
                  path('student_view_project',views.student_submit_project,name="student_submit_project"),
                  #学生查看成绩
                  path('student_view_score',views.student_view_score,name="student_view_score"),
                  #学生查看选题详情
                  path('student_view_project_detail/<str:id>',views.student_view_project_detail,name="student_view_project_detail"),
                  #学生查看审核结果
                  path('student_view_project_ischoosen',views.student_view_project_ischoosen,name="student_view_project_ischoosen"),
                  #学生查看审核结果详情
                  path('student_view_project_ischoosendetail',views.student_view_project_ischoosendetail,name="student_view_project_ischoosendetail"),                 
                  
                  #教师查看选题：教师编辑选题完毕点击“发布”后触发或点击左侧功能栏中“毕业设计”下的“点击查看选题”触发
                  path('teacher_submit_project',views.teacher_submit_project,name="teacher_submit_project"),                
                  #教师编辑选题界面：点击“发布新选题”触发
                  path('teacher_edit_project',views.teacher_edit_project,name="teacher_edit_project"),
                  #教师查看题目详情：点击查看选题界面中的某一个选题触发
                  path('teacher_view_project_detail',views.teacher_view_project_detail,name="teacher_view_project_detail"),                
                  #教师修改选题界面：在查看题目详情界面点击“修改”按钮触发，修改后点击“确定修改”按钮后跳转到查看题目详情界面
                  path('teacher_change_project',views.teacher_change_project,name="teacher_change_project"),                
                  #教师删除选题功能：在查看题目详情界面点击“删除”按钮触发，删除后跳转到教师查看选题界面
                  path('teacher_delete_project',views.teacher_delete_project,name="teacher_delete_project"),                

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
                  path('teacher_ref_student',views.teacher_ref_student,name="teacher_ref_student"),

                  path('teacher_acc_student',views.teacher_acc_student,name="teacher_acc_student"),
                  # 管理员查看选题情况
                  path('adm_projectSelection', views.adm_projectSelection, name="adm_projectSelection"),

]
