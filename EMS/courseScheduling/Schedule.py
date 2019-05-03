import numpy as np
import heapq
#输入
from scoreManagement.models import MajorCourses as MajorCourses
from scoreManagement.models import Teaching as original_Teaching
from backstage.models import ClassRoom, Student, AdmClass, MajorPlan
#输出
from courseScheduling.models import Schedule_result, Teacher_Schedule_result
class Student :
    def __init__(self, id, name, major, year, admclass):
        self.id = id
        self.name = name
        self.major = major
        self.year = year
        self.Admclass = admclass
        #8行14列
        self.courseSchedule = []
        self.examSchedule = []
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')

class Classroom :
    def __init__(self, id, type, container):
        self.id = id
        self.container = container
        self.type = type
        #8行14列
        self.courseSchedule = []
        #8行14列
        self.examSchedule = []
        self.time_count = 0
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')

    def __lt__(self, other):  # operator <
        return self.time_count < other.time_count
    def __ge__(self, other):  # oprator >=
        return self.time_count >= other.time_count
    def __le__(self, other):  # oprator <=
        return self.time_count <= other.time_count
    def __cmp__(self, other):
        # call global(builtin) function cmp for int
        return cmp(self.time_count, other.time_count)

    def update_empty_count(self):
        cnt = 0
        for i in range(1, 8):
            for j in range(0, 13):
                if time_block != '':
                    time_block = self.courseSchedule[i][j].split(',')
                    for block in time_block:
                        l = int(block.split('-')[0])
                        r = int(block.split('-')[1])
                        cnt += (r - l + 1)
        self.empty_count = cnt

class Teacher(object) :
    def __init__(self, id, name):
        self.id = id
        self.name = name
        #8行14列
        self.courseSchedule = []
        #8行14列
        self.examSchedule = []
        self.time_count = 0
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')
    def __lt__(self, other):  # operator <
        return self.time_count < other.time_count
    def __ge__(self, other):  # oprator >=
        return self.time_count >= other.time_count
    def __le__(self, other):  # oprator <=
        return self.time_count <= other.time_count
    def __cmp__(self, other):
        # call global(builtin) function cmp for int
        return cmp(self.time_count, other.time_count)

    def update_empty_count(self):
        cnt = 0
        for i in range(1,8):
            for j in range(0,13):
                if time_block !='':
                    time_block = self.courseSchedule[i][j].split(',')
                    for block in time_block:
                        l = int(block.split('-')[0])
                        r = int(block.split('-')[1])
                        cnt += (r-l+1)
        self.time_count = cnt



class Buffer :
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classrooms = []
        # 8行14列
        self.courseSchedule = []
        # 8行14列
        self.examSchedule = []
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')

Students_id = dict()
Teachers_id = dict()
Classrooms_id = dict()
Courses_id = dict()

def merge_str(str1:str, str2:str):
    str1_split = str1.split(',')
    str2_split = str2.split(',')
    if str1_split[0].__len__() == 0 :
        return str2
    if str2_split[0].__len__() == 0 :
        return str1
    week_block = np.zeros(14)
    for e in str1_split + str2_split:
        l = int(e.split('-')[0])
        r = int(e.split('-')[1])
        for i in range(l, r+1):
            week_block[i] = 1
    res = ''
    flag = 0
    l = 0
    r = 0
    for index, e in enumerate(week_block):
        if flag == 0 and e == 1:
            l = index
            r = index
            flag = 1
        if flag == 1 and e == 1:
            r += 1
        if (flag == 1 and e == 0) or (index == len(week_block)-1 and flag == 1):
            flag = 0
            block = str(l) + '-' + str(r)
            if len(res) == 0:
                res += block
            else:
                res += (','+block)
    return  res

def mergeTable(table1, table2):
    global Classrooms_id, Teachers_id, Students_id, Courses_id
    res = []
    for i in range(8):
        res.append([])
        for j in range(14):
            res[i].append('')
    for i in range(8):
        for j in range(14):
            res[i][j] = merge_str(table1[i][j], table2[i][j])
    return res

def String_to_table(string1:str):
    res = []
    for i in range(8):
        res.append([])
        for j in range(14):
            res[i].append('')
    for block in string1.split(','):
        block_split = block.split('-')
        week_time = block_split[2] + '-' + block_split[3]
        weekday = int(int(block_split[0])/13)
        weekday_start = int(block_split[0]) % 13
        weekday_end = int(block_split[1]) % 13
        if weekday_end == 0:
            weekday_end = 13
        for day in range(weekday_start, weekday_end+1):
            res[weekday][day] = week_time
    return  res


def init():
    year = 2019
    semester = 2
    "目前只有自动排课"
    set1 = Teacher_Schedule_result.objects.filter(cno__year=year, cno__semester=semester)
    for elements in set1:
        Table = String_to_table(elements.time)
        if Classrooms_id.get(elements.where.crno) == None:
            room = Classroom(elements.where.crno, elements.where.crtype, elements.where.contain_num)
            room.courseSchedule = Table
            room.update_empty_count()
            Classrooms_id[elements.where.crno] = room
        else:
            room = Classrooms_id.get(elements.where.crno)
            #这一步可优化
            room.courseSchedule = mergeTable(room.courseSchedule, Table)
            room.update_empty_count()
        if Teachers_id.get(elements.tno.tno.username) == None:
            tcher = Teacher(elements.tno.tno.username, elements.tno.tno.name)
            tcher.courseSchedule = Table
            tcher.update_empty_count()
            Teachers_id[elements.tno.tno.username] = tcher
        else:
            tcher = Teachers_id.get(elements.tno.tno.username)
            tcher.courseSchedule = mergeTable(tcher.courseSchedule, Table)
            tcher.update_empty_count()
        if Courses_id.get(elements.cno.cno.cno+elements.cno.mno.major.mno+str(elements.cno.mno.year)) == None:
            Courses_id[elements.cno.cno.cno+elements.cno.mno.major.mno+str(elements.cno.mno.year)] = True
    set2 = Schedule_result.objects.filter(cno__year=year, cno__semester=semester)
    for elements in set2:
        Table =String_to_table(elements.time)
        if Students_id.get(elements.sno.username) == None:
            stu = Student(elements.sno.username, elements.sno.name,
                          elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
            Students_id[elements.sno.username] = stu
            stu.courseSchedule = Table
        else:
            stu.courseSchedule = mergeTable(stu.courseSchedule, Table)

def autoSchedule():
    year = 2019
    semester = 2
    init()
    #1找课 2找老师 3找学生 4找教室 5生成并检查 6写入数据库
    coures_set = MajorCourses.objects.filter(year=year, semester=semester)
    for coures in coures_set:
        teacher_set = original_Teaching.objects.filter(mcno__cno__cno=coures.cno.cno)
        students_set = Student.objects.filter(in_cls__major=coures.mno)
        if len(students_set) > 200:
            pass


if __name__ == '__main__':
    print("ss")














