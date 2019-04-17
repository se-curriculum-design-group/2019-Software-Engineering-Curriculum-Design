# 2019年软件工程课程设计--成绩管理子系统开发分支

Author: LuoD
---

## 描述

创建了基本的表格与和成绩管理相关的表格，搭建了项目基础框架。

包括学生、教师、课程、专业、学院、专业计划、专业课程计划、教师授课表。

![course](EMS/utils/imgs/img1.png)

![usage](EMS/utils/imgs/img2.png)

## backstage中的表

![backstage_table](EMS/utils/imgs/backstageModel.png)

## scoreManagement中的表

![scoreManagement_tables](EMS/utils/imgs/score_manage.png)

## 用法

1. 删除`backstage`和`scoreManagement`下面的迁移文件。重新生成迁移文件。
2. 进入MySQL数据库，`create database ems2`（为了测试，这里用的是`ems2`）。
3.
```
(Webdev) C:\Users\LuoD\Documents\Repos\2019-Software-Engineering-Curriculum-Design\EMS>python manage.py makemigrations
Migrations for 'backstage':
  backstage\migrations\0001_initial.py
    - Create model AdmClass
    - Create model ClassRoom
    - Create model College
    - Create model Major
    - Create model MajorPlan
    - Create model Student
    - Create model Teacher
    - Add field major to admclass
    - Alter unique_together for majorplan (1 constraint(s))
Migrations for 'scoreManagement':
  scoreManagement\migrations\0001_initial.py
    - Create model AllCourseTable
    - Create model Course
    - Create model MajorCourses
    - Create model Teaching
    - Alter unique_together for majorcourses (1 constraint(s))

(Webdev) C:\Users\LuoD\Documents\Repos\2019-Software-Engineering-Curriculum-Design\EMS>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, backstage, captcha, contenttypes, scoreManagement, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying backstage.0001_initial... OK
  Applying captcha.0001_initial... OK
  Applying scoreManagement.0001_initial... OK
  Applying sessions.0001_initial... OK

(Webdev) C:\Users\LuoD\Documents\Repos\2019-Software-Engineering-Curriculum-Design\EMS>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, backstage, captcha, contenttypes, scoreManagement, sessions
Running migrations:
  No migrations to apply.


```
4. MySQL中运行`source ems.sql`。即可将数据导入数据库中。
5. 进入交互式IPython进行测试。

```
(Webdev) C:\Users\LuoD\Documents\Repos\2019-Software-Engineering-Curriculum-Design\EMS>python manage.py shell
Python 3.6.7 (default, Feb 28 2019, 07:28:18) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: cd utils/database_utils/
C:\Users\LuoD\Documents\Repos\2019-Software-Engineering-Curriculum-Design\EMS\utils\database_utils

In [2]: run add_college.py

In [3]: len(Student.objects.all())
Out[3]: 649

In [4]: len(Teacher.objects.all())
Out[4]: 1159

```
