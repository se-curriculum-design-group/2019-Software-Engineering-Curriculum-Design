from django.shortcuts import render
from django.http import HttpResponse
from backstage.models import User,Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom
from graduationManagement.models import GraduationProject
from django.views.decorators.csrf import csrf_exempt


def welcome(request):
    return render(request, 'graduationManagement/welcome.html')


def graduation_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'graduationManagement/student_graduation_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'graduationManagement/teacher_graduation_manage.html')
    else:
        return render(request, 'graduationManagement/adm_graduation_manage.html')
def student_choose_project(request):
	return render(request,'graduationManagement/student_choose_project.html')

def student_submit_project(request):
	return render(request,'graduationManagement/student_submit_project.html')

def student_view_score(request):
	return render(request,'graduationManagement/student_view_score.html')
#学生查看选题详情
def student_view_project_detail(request):
    return render(request,'graduationManagement/student_view_project_detail.html')   
#学生查看审核结果
def student_view_project_ischoosen(request):
    return render(request,'graduationManagement/student_view_project_ischoosen.html')   
#学生查看审核结果详情
def student_view_project_ischoosendetail(request):
    return render(request,'graduationManagement/student_view_project_ischoosendetail.html')   
def teacher_edit_project(request):
    return render(request,'graduationManagement/teacher_edit_project.html')   
#教师提交选题：增
@csrf_exempt
def teacher_submit_project(request):
    #获取当前老师的id号：当前操作者是谁
    username = request.session['username']
    uno=User.objects.get(username=username)
    tno=Teacher.objects.get(user_ptr_id=uno)
    if request.method == 'POST':
        #获取当前用户输入的信息
        name=request.POST.get('project_name')
        difficulty=request.POST.get('project_difficulty')
        ptype=request.POST.get('project_type')
        descripe=request.POST.get('project_descripe')
        require=request.POST.get('project_requirments')
        #将输入的数据存储到数据库中
        GraduationProject.objects.create(pname=name,tno=tno,pdirection=ptype,pdifficulty=difficulty,pdescription=descripe,pstu=require)
    #从数据库中取数据显示到网页上
    info=GraduationProject.objects.filter(tno=tno)
    contenxt={
        'info':info,
    }
    return render(request,"graduationManagement/teacher_submit_project.html",contenxt)
    # return render(request,'graduationManagement/teacher_edit_project.html')
#教师查看选题详情
def teacher_view_project_detail(request):
     #获取当前老师的id号：当前操作者是谁
    username = request.session['username']
     #将输入的数据存储到数据库中
    uno=User.objects.get(username=username)
    tno=Teacher.objects.get(user_ptr_id=uno)
    id=request.GET.get('id')
     #从数据库中取数据显示到网页上
    info=GraduationProject.objects.filter(tno=tno,id=id)
    contenxt={
        'info':info,
    }
    return render(request,'graduationManagement/teacher_view_project_detail.html',contenxt)   
#教师审核学生
def teacher_choose_student(request):
    return render(request,'graduationManagement/teacher_choose_student.html') 
#教师查看学生提交的文件
def teacher_view_projectfiles(request):
    return render(request,'graduationManagement/teacher_view_projectfiles.html')  
#教师查看学生提交的文件详情
def teacher_view_projectfiles_detail(request):
    return render(request,'graduationManagement/teacher_view_projectfiles_detail.html')  
#教师提交成绩
def teacher_submit_score(request):
    return render(request,'graduationManagement/teacher_submit_score.html')   
#教师提交成绩详情
def teacher_submit_score_detail(request):
    return render(request,'graduationManagement/teacher_submit_score_detail.html')   

