from django.shortcuts import render, redirect
from django.http import HttpResponse
from backstage.models import User, Teacher, Student, \
    College, MajorPlan, AdmClass, ClassRoom
from graduationManagement.models import GraduationProject,StuChoice,Student
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie 

from django.contrib import messages
@csrf_exempt
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

    info = GraduationProject.objects.all()
    sno = request.session['username'] 
    #print(sno)#2016000001
    uno = User.objects.get(username=sno)
    tno = Student.objects.get(user_ptr_id=uno)
    m=tno.user_ptr_id #1
    print(m)
    s=StuChoice.objects.filter(sno_id=m)
    if s:
        l=s[0].pno.id
        ins = GraduationProject.objects.filter(id=l)
        # print(l)
        contenxt = {
            'info': info,
             'ins':ins,
        }
        return render(request, 'graduationManagement/student_choose_project.html',contenxt)
    else:
        contenxt = {
            'info': info,
        }
        return render(request, 'graduationManagement/student_choose_project2.html',contenxt)


def student_submit_project(request):
    return render(request, 'graduationManagement/student_submit_project.html')


def student_view_score(request):
    return render(request, 'graduationManagement/student_view_score.html')




def  student_delete(request):
    id = request.GET.get('id') 
    obj = GraduationProject.objects.get(id=id)
    obj.pstatus = 0
    obj.save()
    s=StuChoice.objects.filter(pno=id)
    if s:
        print(s)
        s.delete()
        # s.save()
    return redirect('graduationManagement:student_choose_project')
#选课动作  
def student_choosing_action(request):
    id = request.GET.get('id')  #课题id
    obj = GraduationProject.objects.get(id=id)
    obj.pstatus = 1
    obj.save()
    #保存 选课状态并设置不可选
    sno = request.session['username']   #2000016
    no = request.session['name'] #姓名
    # uno = User.objects.get(username=sno)    #201600001
    sno_id = Student.objects.get(name=no)
    print(sno_id)
    tno=obj.tno_id
    tno_id=Teacher.objects.get(user_ptr_id=tno)
    pno_id=GraduationProject.objects.get(id=id)
    print(sno_id,tno_id,pno_id)
    ob =StuChoice.objects.create(status=0,sno=sno_id,pno=pno_id,tno=tno_id)    #2拒绝  1被接受  0未审核 

    # ob.save()

     # article = models.Article(title='abc',content='111')
    # category = models.Category(name='最新文章')
    # category.save()
    # article.category = category
    # article.save()
    return redirect('graduationManagement:student_choose_project')



# 学生查看选题详情
def student_view_project_detail(request, id):
    print(request.method)
    info = GraduationProject.objects.filter(pname=id)
    pstatus=GraduationProject.objects.get(pname=id).pstatus
    if pstatus==1:
        messages.success(request, "此课题已被选")
        return redirect('graduationManagement:student_choose_project')

    else:
        return render(request, 'graduationManagement/student_view_project_detail.html', {'info': info})
    # return HttpResponse('test'+id)
    # print(name)
    # if request.method == 'POST':
    #     print(1)
    #     if request.is_ajax():
    #         pname=request.POST.get('s')
    #         # p = GraduationProject.objects.get(pname=m)
    #         # print(type(pname))
    #         print(pname)
    #         # print(len(pname))
    #             # tno = Teacher.objects.get(user_ptr_id=p.tno_id).name
    #         info = GraduationProject.objects.filter(pname=pname)
    #         return 'mytest'
    #         # contenxt = {
    #         #   'info': info,
    #         #   }
    #         # return render(request, 'graduationManagement/student_view_project_detail.html')
    #     return render(request, 'graduationManagement/test.html', {'info': info})
    # else:
    #     return HttpResponse(1) 


# 学生查看审核结果
def student_view_project_ischoosen(request):
    return render(request, 'graduationManagement/student_view_project_ischoosen.html')


# 学生查看审核结果详情
def student_view_project_ischoosendetail(request):
    return render(request, 'graduationManagement/student_view_project_ischoosendetail.html')


# 教师编辑选题界面：点击“发布新选题”触发
def teacher_edit_project(request):
    return render(request, 'graduationManagement/teacher_edit_project.html')


# 教师查看选题：教师编辑选题完毕点击“发布”后触发或点击左侧功能栏中“毕业设计”下的“点击查看选题”触发
@csrf_exempt
def teacher_submit_project(request):
    # 获取当前老师的id号：当前操作者是谁
    username = request.session['username']
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno)
    if request.method == 'POST':
        # 获取当前用户输入的信息
        name = request.POST.get('project_name')
        difficulty = request.POST.get('project_difficulty')
        ptype = request.POST.get('project_type')
        descripe = request.POST.get('project_descripe')
        require = request.POST.get('project_requirments')
        GraduationProject.objects.get(pname=name).delete()
        if 'change' not in request.path:
            # 将输入的数据存储到数据库中
            GraduationProject.objects.create(pname=name, tno=tno, pdirection=ptype, pdifficulty=difficulty,
                                             pdescription=descripe, pstu=require)
        else:
            GraduationProject.objects.filter(tno=tno, id=id).update(pname=project_name)
            GraduationProject.objects.filter(tno=tno, id=id).update(pdirection=ptype)
            GraduationProject.objects.filter(tno=tno, id=id).update(pdifficulty=difficulty)
            GraduationProject.objects.filter(tno=tno, id=id).update(pdescription=project_descripe)
            GraduationProject.objects.filter(tno=tno, id=id).update(pstu=require)
        # 从数据库中取数据显示到网页上
    info = GraduationProject.objects.filter(tno=tno)
    contenxt = {
        'info': info,
    }
    return render(request, "graduationManagement/teacher_submit_project.html", contenxt)
    # return render(request,'graduationManagement/teacher_edit_project.html')


# 教师查看选题详情：点击查看选题界面中的某一个选题触发
def teacher_view_project_detail(request):
    # 获取当前老师的id号：当前操作者是谁
    username = request.session['username']
    # 将输入的数据存储到数据库中
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno)
    id = request.GET.get('id')
    # 从数据库中取数据显示到网页上

    info = GraduationProject.objects.filter(tno=tno, id=id)
    contenxt = {
        'info': info,
    }
    return render(request, 'graduationManagement/teacher_view_project_detail.html', contenxt)


# 教师修改选题界面：在查看题目详情界面点击“修改”按钮触发，修改后点击“确定修改”按钮后跳转到查看题目详情界面
def teacher_change_project(request):
    # 获取当前老师的id号：当前操作者是谁
    username = request.session['username']
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno)
    id = request.GET.get('id')

    info = GraduationProject.objects.filter(tno=tno, id=id)

    contenxt = {
        'info': info,
    }
    return render(request, 'graduationManagement/teacher_change_project.html', contenxt)
    # return redirect('graduationManagement:teacher_view_project_detail')


# 教师删除选题功能：在查看题目详情界面点击“删除”按钮触发，删除后跳转到教师查看选题界面
def teacher_delete_project(request):
    # 获取当前老师的id号：当前操作者是谁
    username = request.session['username']
    # 将输入的数据存储到数据库中
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno)
    id = request.GET.get('id')
    # 从数据库中取数据显示到网页上
    GraduationProject.objects.filter(tno=tno, id=id).delete()

    return redirect('graduationManagement:teacher_submit_project')


# 教师审核学生
def teacher_choose_student(request):
    username = request.session['username']
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno).user_ptr_id
    # return HttpResponse(111)
    # info=GraduationProject.objects.filter(tno_id=tno)
    info=StuChoice.objects.filter(tno_id=tno)
    # print(uno,tno,info)
    contenxt = {
        'info': info,
    }
    return render(request, 'graduationManagement/teacher_choose_student.html',contenxt)

#接受
def teacher_acc_student(request):
    id = request.GET.get('id') 
    print(id)   #8  
    s=StuChoice.objects.get(pno=id)
    s.status=1
    s.save()
    inf= GraduationProject.objects.filter(id=id)
    inf.pstatus=0
    # print(sid)
    username = request.session['username']
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno).user_ptr_id
    info=StuChoice.objects.filter(tno_id=tno)
    # print(uno,tno,info)
    contenxt = {
        'info': info,
    }
    return render(request, 'graduationManagement/teacher_choose_student.html',contenxt) 
#拒绝
def teacher_ref_student(request):
    id = request.GET.get('id') 
    print(id)   #8  
    s=StuChoice.objects.get(pno=id).delete()
    # print(sid)
    inf= GraduationProject.objects.get(id=id)
    inf.pstatus=0
    inf.save()
    username = request.session['username']
    uno = User.objects.get(username=username)
    tno = Teacher.objects.get(user_ptr_id=uno).user_ptr_id
    info=StuChoice.objects.filter(tno_id=tno)
    # print(uno,tno,info)
    contenxt = {
        'info': info,
    }
    return render(request, 'graduationManagement/teacher_choose_student.html',contenxt) 
# 教师查看学生提交的文件
def teacher_view_projectfiles(request):
    return render(request, 'graduationManagement/teacher_view_projectfiles.html')


# 教师查看学生提交的文件详情
def teacher_view_projectfiles_detail(request):
    return render(request, 'graduationManagement/teacher_view_projectfiles_detail.html')


# 教师提交成绩
def teacher_submit_score(request):
    return render(request, 'graduationManagement/teacher_submit_score.html')


# 教师提交成绩详情
def teacher_submit_score_detail(request):
    return render(request, 'graduationManagement/teacher_submit_score_detail.html')

def adm_projectSelection(request):
    return render(request, 'graduationManagement/adm_projectSelection.html')



