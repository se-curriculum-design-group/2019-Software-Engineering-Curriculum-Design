# 2019-Software-Engineering-Curriculum-Design

## 项目骨架 Project Structure

项目骨架已经构建好，采用的一个Project内，多个APP的机制。分别为5个子系统创建
了各自的子APP。

```
$tree EMS
EMS
   | backstage/
   |---- __init__.py
   |----   migrations/
   |----   apps.py
   |----   models.py
   |     ...
   | courseScheduling/
   |---- __init__.py
   |----   migrations/
   |----   apps.py
   |----   models.py
   |     ...
   | courseSelection/
   |---- __init__.py
   |----   migrations/
   |----   apps.py
   |----   models.py
   |     ...
   | graduationManagement/
   |---- __init__.py
   |----   migrations/
   |----   apps.py
   |----   models.py
   |     ...
   | scoreManagement/
   |---- __init__.py
   |----   migrations/
   |----   apps.py
   |----   models.py
   |     ...
            
```

为便于后期的开发和和整体项目的集成，建议采用新建分支的方法来管理和开发。
1. 每个小组一个分支，分支上保存可以完整运行的整个系统的代码。
2. 小组在各自的分支上进行开发，方便后期merge。

## 使用方法 Usage

1. 下载或clone项目
```
git clone https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design.git
```
2. 安装`pymysql`或`mysqlclient`，安装`django-simple-captcha`，用于生成验证码。
```
$ pip install pymysql
$ # or pip install mysqlclient # 我的机器报错不晓得为啥-_-!
$ pip install django-simple-captcha
```
3. 数据库中创建用户和数据库
```
$ mysql -uroot -p
Enter your password: xxxxxx
mysql> create database EMS;
mysql> create user 'EMS'@'localhost' identified by 'password';
mysql>  grant all on *.* to 'EMS'@'localhost';
mysql> flush privileges;
```
4. 用PyCharm打开内部EMS文件夹。删除backstage模块migrations文件夹下除`__init__.py`的文件。重新生成迁移文件。
```
$ python manage.py makemigrations backstage  # 重新生成迁移文件。
$ python manage.py migrate  # 模型迁移到数据库中
$ python manage.py runserver  # 运行服务
```
成功运行没有报错的话，打开 http://127.0.0.1:8000/ 访问。


各小组分支名称如下：

| 模块名称 | 分支名称 |
| :--- | :--- |
| 后台管理子系统 | [backstage](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/backstage) |
| 成绩管理子系统 | [scoreManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/scoreManagement) |
| 毕业设计子系统 | [graduationManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/graduationManagement) |
| 选课子系统 | [courseSelection](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseSelection) |
| 排课子系统 | [courseScheduling](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseScheduling) |

更多项目信息，请查看[wiki](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/wiki)。
