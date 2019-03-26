# 2019-Software-Engineering-Curriculum-Design

## 项目骨架

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

各小组分支名称如下：

| 模块名称 | 分支名称 |
| :--- | :--- |
| 后台管理子系统 | [backstage](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/backstage) |
| 成绩管理子系统 | [scoreManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/scoreManagement) |
| 毕业设计子系统 | [graduationManagement](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/graduationManagement) |
| 选课子系统 | [courseSelection](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseSelection) |
| 排课子系统 | [courseScheduling](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/tree/courseScheduling) |

更多项目信息，请查看[wiki](https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design/wiki)。
