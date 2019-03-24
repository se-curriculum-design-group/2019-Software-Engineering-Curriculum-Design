为便于后期的开发和和整体项目的集成，建议采用新建分支的方法来管理和开发。
1. 每个小组一个分支，分支上保存可以完整运行的整个系统的代码。
2. 小组在各自的分支上进行开发，方便后期merge。

各小组分支名称如下：

| 模块名称 | 分支名称 |
| :--- | :--- |
| 后台管理子系统 | [backstage](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/backstage) |
| 成绩管理子系统 | [scoreManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/scoreManagement) |
| 毕业设计子系统 | [graduationManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/graduationManagement) |
| 选课子系统 | [courseSelection](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseSelection) |
| 排课子系统 | [courseScheduling](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseScheduling) |


# 2019-Software-Engineering-Curriculum-Design

Welcome! Code is comming soon~

------

# 2019/03/15第一次会议记录

参会人员：罗登，何显，蔡锐，张云皓。

## 会议内容

### 语言及框架选定
经过较长时间的讨论，大家各抒己见，说明了自己小组的情况和水平，最终考虑大多数同学都有Python及Django开发基础，因此选的开发语言为Python3.60，Django2.1，数据库为MySql8.0。通过git进行版本控制，github进行项目管理。

| 语言 | 框架 | 数据库 | 版本控制 | 项目管理 |
| :----: | :----: | :----: | :----: | :----: |
|[Python3.6](https://www.python.org/) | [Django2.1](https://www.djangoproject.com/) | [MySql8.0](https://www.mysql.com/) | Git | [项目地址](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design) |

### 小组选题

通过自选和抽签等方式确定选题：

| 题目 | 分配小组 |
| :---: | :---: |
| 后台管理子系统 | [蔡锐小组](https://github.com/software-engineering-backstage-team) |
| 排课子系统 | [罗登小组](https://github.com/RonDen/Course-Scheduling-System) |
| 成绩管理子系统 | [张云皓小组](https://github.com/MegamanZeroX/SoftwareEngineering) |
| 毕业设计管理子系统 | [朱迪迪小组](https://github.com/Invisibleee/Graduation-project-management-system) |
| 选课子系统 | [何显小组](https://github.com/Messiahhhh/2019-Software-Engineering-Curriculum-Design--) |

### 后续工作安排
1. 及时向团长提交小组名单。
2. 小组长要学会Git和github的基本使用。在github上创建好各自小组的仓库。
3. 了解和学习Python编码规范。_i.e._ Python增强议案[PEP8](https://www.python.org/dev/peps/pep-0008/)，Python代码分析检查工具[Flake8](http://flake8.pycqa.org/en/latest/)，[Pylint](https://www.pylint.org/)等。以上工具均在PyCharm或[VS Code](https://code.visualstudio.com/)中有集成或者提供插件下载，十分方便。
4. 了解软件测试相关内容，[pytest](https://pytest.org/)等模块。

### 下次开会时间

暂定下周五晚上最后一节课下课。

### 相关学习资料链接

- [菜鸟教程git教程](http://www.runoob.com/git/git-tutorial.html)
- [廖雪峰git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)


# 2019/03/22第二次会议记录

参会人员：罗登，蔡锐，朱迪迪，何显，张云皓

## 会议讨论内容

1. 沟通目前各小组内部分工情况。是否有召集线下会议。
2. 各小组长轮流发言，描述各自模块功能。约定在**下周**提交**小组功能分析说明**。
3. 选定合适的前端框架，辅助的前端设计人员。
4. 后台数据库内容。数据库访问方式等。
5. 分析数据流图，各视图下数据流动方向。

## 补充

- 各小组长在本项目master分支上建立新的分支，将各自小组的项目同步到新的分支上开发，便于集成测试与整体项目监控。
- 前端建议了解[Vue.js](https://cn.vuejs.org/), [Bootstrap](http://www.runoob.com/bootstrap/bootstrap-tutorial.html), [AdminTable](https://adminlte.io/), [Echarts.js](https://echarts.baidu.com/)等。
