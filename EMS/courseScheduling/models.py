from django.db import models
from backstage.models import Student, Teacher
from scoreManagement.models import Teaching, MajorCourses, ClassRoom
from backstage.models import Student, Teacher, ClassRoom


class Schedule_result(models.Model):
    """
        凡是被加在这里的数据，一定是有学生，老师，教室，时间地点已定。
        第一次自动排完后，只有必修课在这里，选修不在，
        选修的同步目前不同步更新
    """
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    def __str__(self):
        return "-".join([self.sno, self.tno, self.where, self.time, ])
    class Meta:
        db_table = 'Schedule_result'
        unique_together = (
            'sno', 'tno', 'where', 'time'
        )


class Teacher_Schedule_result(models.Model):
    tno = models.ForeignKey(to=Teaching, on_delete=models.CASCADE)
    where = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    time = models.CharField(max_length=128, null=False)
    current_number = models.IntegerField()
    MAX_number = models.IntegerField()
    state = models.CharField(max_length=128)

    def __str__(self):
        return "-".join([self.tno, self.where, self.time, ])
    class Meta:
        db_table = 'Teacher_Schedule_result'
        unique_together = (
              'tno', 'where', 'time'
        )

"""
2019-05-08 20:43:00 0x484c Error in foreign key constraint of table ems/#sql-17bc_6cd:
 FOREIGN KEY (`where_id`) REFERENCES `class_room` (`crno`):
Cannot find an index in the referenced table where the
referenced columns appear as the first columns, or column types
in the table and the referenced table do not match for constraint.
Note that the internal storage type of ENUM and SET changed in
tables created with >= InnoDB-4.1.12, and such columns in old tables
cannot be referenced by such columns in new tables.
Please refer to http://dev.mysql.com/doc/refman/8.0/en/innodb-foreign-key-constraints.html for correct foreign key definition.

/*建立连接使用的编码*/
set character_set_connection=utf8;
/*数据库的编码*/
set character_set_database=utf8;
/*结果集的编码*/
set character_set_results=utf8;
/*数据库服务器的编码*/
set character_set_server=utf8mb4;

set character_set_system=utf8mb4;

set collation_connection=utf8mb4;

set collation_database=utf8mb4;

set collation_server=utf8mb4;

修改全局字符集
"""