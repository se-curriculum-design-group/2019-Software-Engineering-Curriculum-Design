import numpy as np
import heapq
# 输入
from scoreManagement.models import MajorCourses as MajorCourses
from scoreManagement.models import Teaching as original_Teaching
from backstage.models import ClassRoom, Student, AdmClass, MajorPlan
# 输出
from courseScheduling.models import Schedule_result, Teacher_Schedule_result


class Student:
    def __init__(self, id, name, major, year, admclass):
        self.id = id
        self.name = name
        self.major = major
        self.year = year
        self.Admclass = admclass
        # 8行14列
        self.courseSchedule = []
        self.examSchedule = []
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')


class Classroom:
    def __init__(self, id, type, container):
        self.id = id
        self.container = container
        self.type = type
        # 8行14列
        self.courseSchedule = []
        # 8行14列
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


class Teacher(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # 8行14列
        self.courseSchedule = []
        # 8行14列
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
        self.time_count = cnt


class Buffer:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classrooms = []
        self.course = ''
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


def merge_str(str1: str, str2: str):
    str1_split = str1.split(',')
    str2_split = str2.split(',')
    if str1_split[0].__len__() == 0:
        return str2
    if str2_split[0].__len__() == 0:
        return str1
    week_block = np.zeros(14)
    for e in str1_split + str2_split:
        l = int(e.split('-')[0])
        r = int(e.split('-')[1])
        for i in range(l, r + 1):
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
        if (flag == 1 and e == 0) or (index == len(week_block) - 1 and flag == 1):
            flag = 0
            block = str(l) + '-' + str(r)
            if len(res) == 0:
                res += block
            else:
                res += (',' + block)
    return res


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


course_2_96 = [(1, 2), (3, 4), (6, 7), (7, 8)]
course_3 = [(1, 3), (3, 5), (6, 8), (8, 10), (11, 13)]
course_2 = [(1, 2), (3, 4), (6, 7), (9, 10), (11, 12)]


def String_to_table(string1: str):
    res = []
    for i in range(8):
        res.append([])
        for j in range(14):
            res[i].append('')
    for block in string1.split(','):
        block_split = block.split('-')
        week_time = block_split[2] + '-' + block_split[3]
        weekday = int(int(block_split[0]) / 13)
        weekday_start = int(block_split[0]) % 13
        weekday_end = int(block_split[1]) % 13
        if weekday_end == 0:
            if weekday != 0:
                weekday -= 1
            weekday_end = 13
        for day in range(weekday_start, weekday_end + 1):
            res[weekday][day] = week_time
    return res


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
            # 这一步可优化
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
        if Courses_id.get(elements.cno.cno.cno + elements.cno.mno.major.mno + str(elements.cno.mno.year)) == None:
            Courses_id[elements.cno.cno.cno + elements.cno.mno.major.mno + str(elements.cno.mno.year)] = True
    set2 = Schedule_result.objects.filter(cno__year=year, cno__semester=semester)
    for elements in set2:
        Table = String_to_table(elements.time)
        if Students_id.get(elements.sno.username) == None:
            stu = Student(elements.sno.username, elements.sno.name,
                          elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
            Students_id[elements.sno.username] = stu
            stu.courseSchedule = Table
        else:
            stu.courseSchedule = mergeTable(stu.courseSchedule, Table)


def check_hazard(weekday, daytime, schedule, week_start, week_end):
    st = daytime[0]
    ed = daytime[1] + 1
    for time in range(st, ed):
        string = str(schedule[weekday][time + weekday * 13])
        for subtime in string.split(','):
            if (int(subtime.split('-')[0]) <= week_start and week_start <= int(subtime.split('-')[1])) or \
                    (int(subtime.split('-')[0]) <= week_end and week_end <= int(subtime.split('-')[1])):
                return False
    return True


def coures_time_generate(schedule, time):
    res = ''
    if time > 70:
        weektime_base = int(time / 6)
        rest = time % 6
        way1 = 1
        for cnt in range(3):
            weektime_cur = weektime_base
            if cnt == 0:
                if rest > 0:
                    rest -= 2
                    weektime_cur += 1
            for i, e in enumerate(course_2_96):
                if check_hazard(cnt * 2, e, schedule, 1, weektime_cur):
                    if len(res) == 0:
                        res += str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    else:
                        res += ',' + str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    break
                elif i == len(course_2_96) - 1:
                    way1 = 0
                    break
        if way1 == 1:
            return res
        else:
            res = ''
            for cnt in range(2):
                weektime_cur = weektime_base
                if cnt == 0:
                    if rest > 0:
                        rest -= 2
                        weektime_cur += 1
                for i, e in enumerate(course_3):
                    if check_hazard(cnt * 2, e, schedule, 1, weektime_cur):
                        if len(res) == 0:
                            res += str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                        else:
                            res += ',' + str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                        break
                    elif i == len(course_3) - 1:
                        return None
            return res
    if 56 <= time and time <= 64:
        way1 = 1
        weektime_base = int(time / 4)
        rest = time % 4
        cnt = 0
        for weekday in range(5):
            weektime_cur = weektime_base
            if rest > 0:
                rest -= 2
                weektime_cur += 1
            for i, e in enumerate(course_2_96):
                if check_hazard(weekday, e, schedule, 1, weektime_cur):
                    if len(res) == 0:
                        res += str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    else:
                        res += ',' + str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    weekday += 1
                    cnt += 1
                    break
            if cnt == 2:
                return res
            if weekday == 4 and cnt < 2:
                way1 = 0
                break
        if way1 == 0:
            weektime_base = int(time / 6)
            for bias in range(7):
                cnt = 0
                rest = time % 6
                for weekday in range(5):
                    weektime_cur = weektime_base
                    if rest > 0:
                        rest -= 2
                        weektime_cur += 1
                    if weektime_cur + bias > 17 and cnt < 2:
                        return None
                for i, e in enumerate(course_3):
                    if check_hazard(weekday, e, schedule, 1 + bias, weektime_cur + bias):
                        if len(res) == 0:
                            res += str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                        else:
                            res += ',' + str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                        weekday += 1
                        cnt += 1
                        break
                if cnt == 2:
                    return res
    if time < 56:
        weektime_base = int(time / 3)
        for bias in range(8):
            cnt = 0
            rest = time % 3
            for weekday in range(5):
                weektime_cur = weektime_base
                if rest > 0:
                    rest -= 3
                    weektime_cur += 1
                if weektime_cur + bias > 17 and cnt < 2:
                    return None
            for i, e in enumerate(course_3):
                if check_hazard(weekday, e, schedule, 1 + bias, weektime_cur + bias):
                    if len(res) == 0:
                        res += str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    else:
                        res += ',' + str(e[0]) + '-' + str(e[1]) + '1' + '-' + str(weektime_cur)
                    weekday += 1
                    cnt += 1
                    break
            if cnt == 2:
                return res


def write_to_database(res: str, bf: Buffer):
    # 字符串 合并到表可进一步优化
    tno_mno = original_Teaching.objects.get(mcno=bf.course, tno__username=bf.teachers[0])
    cur_num = 0
    ctype = tno_mno.mcno.cno.course_type
    if ctype == '必修':
        cur_num = len(bf.students)
    TSr = Teacher_Schedule_result.objects.create(
        tno=tno_mno,
        where=ClassRoom.objects.get(crno=bf.classrooms[0]),
        time=res,
        current_number=cur_num,
        MAX_number=len(bf.students),
        state=tno_mno.mcno.cno.course_type,
    )
    table = String_to_table(res)
    bf.teachers[0].courseSchedule = mergeTable(bf.teachers[0].courseSchedule, table)
    bf.classrooms[0].courseSchedule = mergeTable(bf.classrooms[0].courseSchedule, table)
    bf.teachers[0].time_count += tno_mno.mcno.hour_total
    bf.classrooms[0].courseSchedule += tno_mno.mcno.hour_total
    TSr.save()
    if ctype == '必修':
        for sno in bf.students:
            Sr = Schedule_result.objects.create(
                sno=Student.objects.get(username=sno),
                tno=tno_mno.tno,
                where=ClassRoom.objects.get(crno=bf.classrooms[0]),
                time=res,
            )
            Sr.save()
            sno.courseSchedule = mergeTable(sno.courseSchedule, table)


def distribute_single(bf: Buffer, room: Classroom, tch: Teacher, course):
    bf.courseSchedule = mergeTable(tch.courseSchedule, bf.courseSchedule)
    bf.courseSchedule = mergeTable(room.courseSchedule, bf.courseSchedule)
    bf.teachers.append(tch.id)
    bf.classrooms.append(room.id)
    res = coures_time_generate(bf.courseSchedule, course.hour_total)
    write_to_database(res, bf)


def autoSchedule():
    year = 2019
    semester = 2
    init()
    # 1找课 2找老师 3找学生 4找教室 5生成并检查 6写入数据库
    heap_bigroom = []
    heap_midroom = []
    heap_smallroom = []
    for key in Classrooms_id:
        elements = Classrooms_id[key]
        if elements.type == '大':
            heapq.heappush(heap_bigroom, elements)
        if elements.type == '中':
            heapq.heappush(heap_midroom, elements)
        if elements.type == '小':
            heapq.heappush(heap_smallroom, elements)
    coures_set = MajorCourses.objects.filter(year=year, semester=semester)
    for course in coures_set:
        teacher_set = original_Teaching.objects.filter(mcno__cno__cno=course.cno.cno)
        heap_teacher = []
        # 教师建堆
        for elements in teacher_set:
            if Teachers_id.get(elements.tno.username) == None:
                tcher = Teacher(elements.tno.usernam, elements.tno.name)
                tcher.update_empty_count()
                Teachers_id[elements.tno.username] = tcher
                heapq.heappush(heap_teacher, tcher)
            else:
                heapq.heappush(heap_teacher, Teachers_id.get(elements.tno.username))
        students_set = Student.objects.filter(in_cls__major=course.mno)
        bf = Buffer()
        bf.course = course
        if len(students_set) > 200:
            class_dic = dict()
            stu_cnt = 0
            for elements in students_set:
                stu = None
                if Students_id.get(elements.sno.username) == None:
                    stu = Student(elements.sno.username, elements.sno.name,
                                  elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.sno.username)
                # 人数达上限分配教师、地点、重置Buffer
                # class_dic班级字典
                if (class_dic.get(stu.in_cls) == None and len(class_dic) == 6) or stu_cnt >= 195:
                    teacher = heap_teacher[0]
                    bf.courseSchedule = mergeTable(teacher.courseSchedule, bf.courseSchedule)
                    bf.teachers.append(teacher.id)
                    classroom = heap_bigroom[0]
                    bf.courseSchedule = mergeTable(classroom.courseSchedule, bf.courseSchedule)
                    bf.classrooms.append(classroom.id)
                    res = coures_time_generate(bf.courseSchedule, course.hour_total)
                    write_to_database(res, bf)
                    # 重置 计数
                    bf = Buffer()
                    bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                    class_dic = dict()
                    class_dic[stu.in_cls] = 1
                    stu_cnt = 1
                    # 更新堆
                    heapq.heapify(heap_teacher)
                    heapq.heapify(classroom)
                else:  # 累计
                    bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                    bf.students.append(stu.id)
                    class_dic[stu.in_cls] = 1
                    stu_cnt += 1
            if len(bf.students) <= 50:
                distribute_single(bf, heap_smallroom[0], heap_teacher[0], course)
                heapq.heapify(heap_teacher)
                heapq.heapify(heap_smallroom)
            elif len(bf.students) >= 50 and len(bf.students) <= 120:
                distribute_single(bf, heap_midroom[0], heap_teacher[0], course)
                heapq.heapify(heap_teacher)
                heapq.heapify(heap_midroom)
            else:
                distribute_single(bf, heap_bigroom[0], heap_teacher[0], course)
                heapq.heapify(heap_teacher)
                heapq.heapify(heap_bigroom)
            # 重置 bf
        elif len(students_set) <= 200 and len(students_set) > 120:
            for elements in students_set:
                if Students_id.get(elements.sno.username) == None:
                    stu = Student(elements.sno.username, elements.sno.name,
                                  elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.sno.username)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            distribute_single(bf, heap_bigroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_bigroom)
        elif len(students_set) <= 120 and len(students_set) > 50:
            for elements in students_set:
                if Students_id.get(elements.sno.username) == None:
                    stu = Student(elements.sno.username, elements.sno.name,
                                  elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.sno.username)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            distribute_single(bf, heap_midroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_midroom)
        elif len(bf.students) <= 50:
            for elements in students_set:
                if Students_id.get(elements.sno.username) == None:
                    stu = Student(elements.sno.username, elements.sno.name,
                                  elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.sno.username)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            distribute_single(bf, heap_smallroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_smallroom)


if __name__ == '__main__':
    print("ss")
