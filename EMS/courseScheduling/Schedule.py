import numpy as np
import heapq
# 输入
from scoreManagement.models import MajorCourses as MajorCourses
from scoreManagement.models import Teaching as original_Teaching
from backstage.models import ClassRoom, Student, AdmClass, MajorPlan
from courseSelection.models import courseSelected as courseSelected
# 输出
from courseScheduling.models import Schedule_result, Teacher_Schedule_result, Classroom_other_schedule, Exam_Schedule

year = 2019
semester = 2


class Students:
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
            for j in range(14):
                self.courseSchedule[i].append('')
        for i in range(7):
            self.examSchedule.append([])
            for j in range(5):
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
        self.exam_time_count = 0
        self.cmp_type = 0
        for i in range(8):
            self.courseSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
        for i in range(7):
            self.examSchedule.append([])
            for j in range(5):
                self.examSchedule[i].append('')

    def __lt__(self, other):  # operator <
        if self.cmp_type == 0:
            return self.time_count < other.time_count
        else:
            return self.exam_time_count < other.exam_time_count

    def __ge__(self, other):  # oprator >=
        if self.cmp_type == 0:
            return self.time_count >= other.time_count
        else:
            return self.exam_time_count >= other.exam_time_count

    def __le__(self, other):  # oprator <=
        if self.cmp_type == 0:
            return self.time_count <= other.time_count
        else:
            return self.exam_time_count <= other.exam_time_count

    def update_empty_count(self):
        cnt = 0
        for i in range(1, 8):
            for j in range(0, 13):
                time_block = self.courseSchedule[i][j]
                if time_block != '':
                    time_block = time_block.split(',')
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
        self.exam_time_count = 0
        self.cmp_type = 0
        for i in range(8):
            self.courseSchedule.append([])
            self.examSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
                self.examSchedule[i].append('')

    def __lt__(self, other):  # operator <
        if self.cmp_type == 0:
            return self.time_count < other.time_count
        else:
            return self.exam_time_count < other.exam_time_count

    def __ge__(self, other):  # oprator >=
        if self.cmp_type == 0:
            return self.time_count >= other.time_count
        else:
            return self.exam_time_count >= other.exam_time_count

    def __le__(self, other):  # oprator <=
        if self.cmp_type == 0:
            return self.time_count <= other.time_count
        else:
            return self.exam_time_count <= other.exam_time_count

    def update_empty_count(self):
        cnt = 0
        for i in range(1, 8):
            for j in range(0, 13):
                time_block = self.courseSchedule[i][j]
                if time_block != '':
                    time_block = time_block.split(',')
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
        self.examSchedule = []
        for i in range(8):
            self.courseSchedule.append([])
            for j in range(14):
                self.courseSchedule[i].append('')
        for i in range(7):
            self.examSchedule.append([])
            for j in range(5):
                self.examSchedule[i].append('')


Students_id = dict()
Teachers_id = dict()
Classrooms_id = dict()
Courses_id = dict()
has_already_scheduled = dict()

def merge_str(str1: str, str2: str):
    str1_split = str1.split(',')
    str2_split = str2.split(',')
    if str1_split[0].__len__() == 0:
        return str2
    if str2_split[0].__len__() == 0:
        return str1
    week_block = np.zeros(21)
    print(str1_split, str2_split)
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
            if r > l:
                r -= 1
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
    for i in range(len(table1)):
        res.append([])
        for j in range(len(table1[i])):
            res[i].append('')
    for i in range(len(table1)):
        for j in range(len(table1[i])):
            res[i][j] = merge_str(table1[i][j], table2[i][j])
    return res


course_2_96 = [(1, 2), (3, 4), (6, 7), (7, 8)]
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
    "目前只有自动排课"
    set1 = Teacher_Schedule_result.objects.filter(tno__mcno__year=year, tno__mcno__semester=semester)
    for elements in set1:
        Table = String_to_table(elements.time)
        if Classrooms_id.get(elements.where.crno) == None:
            room = Classroom(elements.where.crno, elements.where.crtype, elements.where.contain_num)
            room.courseSchedule = Table
            time_occupy_in_other = Classroom_other_schedule.objects.filter(crno=elements.where)
            print(time_occupy_in_other)
            if len(time_occupy_in_other) > 0:
                for time_block in time_occupy_in_other:
                    room.courseSchedule = mergeTable(room.courseSchedule, String_to_table(time_block.time))
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
        if Courses_id.get(elements.tno.mcno.cno.cno + elements.tno.mcno.mno.major.mname
                          + elements.tno.tno.username) == None:
            Courses_id[elements.tno.mcno.cno.cno + elements.tno.mcno.mno.major.mname
                       + elements.tno.tno.username] = True
        elements_in_courseSelection = courseSelected.objects.filter(cno=elements)
        for element in elements_in_courseSelection:
            stu_table = String_to_table(element.cno.time)
            if Students_id.get(element.sno.username) == None:
                stu = Students(element.sno.username, element.sno.name,
                               element.sno.in_cls.major.major.mno, element.sno.in_year, element.sno.in_cls.name)
                Students_id[elements.sno.username] = stu
                stu.courseSchedule = stu_table
            else:
                Students_id[element.sno.username].courseSchedule = mergeTable(
                    Students_id[element.sno.username].courseSchedule, stu_table)
        if has_already_scheduled.get(elements.tno.mcno.cno.cno+elements.tno.mcno.mno.major.mname) == None:
            has_already_scheduled[elements.tno.mcno.cno.cno+elements.tno.mcno.mno.major.mname] = True

    set2 = Schedule_result.objects.filter(tno__mcno__year=year, tno__mcno__semester=semester)
    for elements in set2:
        Table = String_to_table(elements.time)
        if Students_id.get(elements.sno.username) == None:
            stu = Students(elements.sno.username, elements.sno.name,
                           elements.sno.in_cls.major.major.mno, elements.sno.in_year, elements.sno.in_cls.name)
            Students_id[elements.sno.username] = stu
            stu.courseSchedule = Table
        else:
            Students_id[elements.sno.username].courseSchedule = mergeTable(
                Students_id[elements.sno.username].courseSchedule, Table)



def check_hazard(weekday, daytime, schedule, week_start, week_end):
    st = daytime[0]
    ed = daytime[1] + 1
    for time in range(st, ed):
        string = str(schedule[weekday][time])
        if len(string) == 0:
            continue
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
                        res += str(e[0] + cnt * 2 * 13) + '-' + str(e[1] + cnt * 2 * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
                    else:
                        res += ',' + str(e[0] + cnt * 2 * 13) + '-' + str(e[1] + cnt * 2 * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
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
                            res += str(e[0] + cnt * 2 * 13) + '-' + str(e[1] + cnt * 2 * 13) + '-' + '1' + '-' + str(
                                weektime_cur)
                        else:
                            res += ',' + str(e[0] + cnt * 2 * 13) + '-' + str(
                                e[1] + cnt * 2 * 13) + '-' + '1' + '-' + str(weektime_cur)
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
                        res += str(e[0] + weekday * 13) + '-' + str(e[1] + weekday * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
                    else:
                        res += ',' + str(e[0] + weekday * 13) + '-' + str(e[1] + weekday * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
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
                            res += str(e[0] + weekday * 13) + '-' + str(e[1] + weekday * 13) + '-' + '1' + '-' + str(
                                weektime_cur)
                        else:
                            res += ',' + str(e[0] + weekday * 13) + '-' + str(
                                e[1] + weekday * 13) + '-' + '1' + '-' + str(weektime_cur)
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
                        res += str(e[0] + weekday * 13) + '-' + str(e[1] + weekday * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
                    else:
                        res += ',' + str(e[0] + weekday * 13) + '-' + str(e[1] + weekday * 13) + '-' + '1' + '-' + str(
                            weektime_cur)
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
    if '必修' in ctype:
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
    Teachers_id.get(bf.teachers[0]).courseSchedule = mergeTable(Teachers_id.get(bf.teachers[0]).courseSchedule, table)
    Classrooms_id.get(bf.classrooms[0]).courseSchedule = mergeTable(Classrooms_id.get(bf.classrooms[0]).courseSchedule,
                                                                    table)
    Teachers_id.get(bf.teachers[0]).time_count += tno_mno.mcno.hour_total
    Classrooms_id.get(bf.classrooms[0]).time_count += tno_mno.mcno.hour_total
    TSr.save()
    if '必修' in ctype:
        for sno in bf.students:
            Sr = Schedule_result.objects.create(
                sno=Student.objects.get(username=sno),
                tno=tno_mno,
                where=ClassRoom.objects.get(crno=bf.classrooms[0]),
                time=res,
            )
            Sr.save()
            Students_id.get(sno).courseSchedule = mergeTable(Students_id.get(sno).courseSchedule, table)


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
    room_set = ClassRoom.objects.all()
    for elements in room_set:
        if Classrooms_id.get(elements.crno) == None:
            Classrooms_id[elements.crno] = Classroom(elements.crno, elements.crtype, elements.contain_num)
        if Classrooms_id[elements.crno].type == '大':
            heapq.heappush(heap_bigroom, Classrooms_id[elements.crno])
        if Classrooms_id[elements.crno].type == '中':
            heapq.heappush(heap_midroom, Classrooms_id[elements.crno])
        if Classrooms_id[elements.crno].type == '小':
            heapq.heappush(heap_smallroom, Classrooms_id[elements.crno])
    coures_set = MajorCourses.objects.filter(year=year, semester=semester)
    for course in coures_set:
        if has_already_scheduled.get(course.cno.cno + course.mno.major.mname) == True:
            continue
        teacher_set = original_Teaching.objects.filter(mcno__cno__cno=course.cno.cno)
        heap_teacher = []
        # 教师建堆
        for elements in teacher_set:
            if Teachers_id.get(elements.tno.username) == None:
                tcher = Teacher(elements.tno.username, elements.tno.name)
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
                if Students_id.get(elements.username) == None:
                    stu = Students(elements.username, elements.name,
                                   elements.in_cls.major.major.mname, elements.sno.in_year, elements.sno.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.username)
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
                if Students_id.get(elements.username) == None:
                    stu = Students(elements.username, elements.username,
                                   elements.in_cls.major.major.mno, elements.in_year, elements.in_cls.name)
                    Students_id[elements.username] = stu
                else:
                    stu = Students_id.get(elements.username)
                print(bf.courseSchedule)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            # print(heap_bigroom, '----', heap_teacher)
            distribute_single(bf, heap_bigroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_bigroom)
        elif len(students_set) <= 120 and len(students_set) > 50:
            for elements in students_set:
                if Students_id.get(elements.username) == None:
                    stu = Students(elements.username, elements.username,
                                   elements.in_cls.major.major.mno, elements.in_year, elements.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.username)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            distribute_single(bf, heap_midroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_midroom)
        elif len(bf.students) <= 50:
            for elements in students_set:
                if Students_id.get(elements.username) == None:
                    stu = Students(elements.username, elements.username,
                                   elements.in_cls.major.major.mno, elements.in_year, elements.in_cls.name)
                    Students_id[elements.sno.username] = stu
                else:
                    stu = Students_id.get(elements.username)
                bf.courseSchedule = mergeTable(stu.courseSchedule, bf.courseSchedule)
                bf.students.append(stu.id)
            distribute_single(bf, heap_smallroom[0], heap_teacher[0], course)
            heapq.heapify(heap_teacher)
            heapq.heapify(heap_smallroom)
            has_already_scheduled[course.cno.cno + course.mno.major.mname] = True

# ---------------------
# 自动排考试时间
"""
1.手动排课（排一些没有排好的课，属于教学活动）
2.查询教室:学生、老师---查询。管理员查+改（添加临时活动1-2，一个上午）。
3.生成课表---》初步的课表---》选课加入课表
"""
# ----------------------------
# 按地点查空闲:
def Search_spare_room(name: str):
    cls = ClassRoom.objects.get(crno=name)
    classroom = Classroom(cls.crno, cls.crtype, cls.contain_num)
    time_occupy_in_Teaching = Teacher_Schedule_result.objects.filter(where__crno=name)
    for element in time_occupy_in_Teaching:
        classroom.courseSchedule = mergeTable(classroom.courseSchedule, String_to_table(element.time))
    time_occupy_in_other = Classroom_other_schedule.objects.filter(crno__crno=name)
    for element in time_occupy_in_other:
        classroom.courseSchedule = mergeTable(classroom.courseSchedule, String_to_table(element.time))
    Classrooms_id[name] = classroom
    return classroom


# 搜索目标房间名的时间空闲:
def Search_spare_room(name: str) -> Classroom:
    cls = ClassRoom.objects.get(crno=name)
    classroom = Classroom(cls.crno, cls.crtype, cls.contain_num)
    time_occupy_in_Teaching = Teacher_Schedule_result.objects.filter(where__crno=name)
    for element in time_occupy_in_Teaching:
        classroom.courseSchedule = mergeTable(classroom.courseSchedule, String_to_table(element.time))
    time_occupy_in_other = Classroom_other_schedule.objects.filter(crno__crno=name)
    for element in time_occupy_in_other:
        classroom.courseSchedule = mergeTable(classroom.courseSchedule, String_to_table(element.time))
    Classrooms_id[name] = classroom
    return classroom


# 搜索时间空闲的房间:
def week_has_hazzard(week1: str, week2: str):
    if len(week1) == 0 or len(week2) == 0:
        return False
    l1 = int(week1.split('-')[0])
    r1 = int(week1.split('-')[1])
    l2 = int(week2.split('-')[0])
    r2 = int(week2.split('-')[1])
    if (l2 <= l1 and l1 <= r2) or (l1 <= l2 and l2 <= r1):
        return True
    else:
        return False


def has_table_hazzard(table1, table2):
    for i in 8:
        if i == 0: continue
        for j in 14:
            if j == 0: continue
        if week_has_hazzard(table1[i][j], table2[i][j]):
            return True
    return False


def Search_time_room(time: str):
    init()
    res = []
    table = mergeTable(time)
    for element in Classrooms_id:
        room = Classrooms_id[element]
        if has_table_hazzard(room.courseSchedule, table):
            continue
        else:
            res.append(room)
    return room


def get_students_teacher_courseSchedule(stuset: [], class_set=None, teacher_username=None) -> Buffer:
    if teacher_username == None:
        return None
    init()
    bf = Buffer()
    if class_set == None:
        for element in stuset:
            stud = None
            if Students_id.get(element) == None:
                stu = Student.objects.get(username=element)
                stud = Students(stu.username, stu.name, stu.in_cls.major, stu.in_year, stu.in_cls.name)
                Students_id[stu.username] = stud
            else:
                stud = Students_id[element]
            bf.courseSchedule = mergeTable(bf.courseSchedule, stud.courseSchedule)
        if Teachers_id[teacher_username] != None:
            bf.courseSchedule = mergeTable(bf.courseSchedule, Teachers_id[teacher_username].courseSchedule)
        return bf
    else:
        bf = Buffer()
        for in_class in class_set:
            stu_set = Student.objects.filter(in_cls__name=in_class)
            for element in stu_set:
                stud = None
                if Students_id.get(element) == None:
                    stu = Student.objects.get(username=element)
                    stud = Students(stu.username, stu.name, stu.in_cls.major, stu.in_year, stu.in_cls.name)
                    Students_id[stu.username] = stud
                else:
                    stud = Students_id[element]
                bf.courseSchedule = mergeTable(bf.courseSchedule, stud.courseSchedule)
        if Teachers_id[teacher_username] != None:
            bf.courseSchedule = mergeTable(bf.courseSchedule, Teachers_id[teacher_username].courseSchedule)
        return bf


# 处理手工排课
def manual_schedule(place_name, time_string, stuset: [], class_set=None, teacher_username=None):
    if class_set == None:
        init()
        if Classrooms_id.get(place_name) == None:
            room = ClassRoom.objects.get(crno=place_name)
            Classrooms_id[place_name] = Classroom(place_name, room.crtype, room.contain_num)
        for stu_sno in stuset:
            if Students_id.get(stu_sno) == None:
                pass

        bf = Buffer()

    else:
        pass

# 排考试时间
def String_to_examTable(string:str):
    res = []
    for i in range(7):
        res.append([])
        for j in range(5):
            res[i].append('')
    res[int(string.split('-')[0])][int(string.split('-')[1])] = '20-20'
    return res

def init_exam():
    rows_in_exam = Exam_Schedule.objects.filter(tno_mno_course__tno__mcno__year=year, tno_mno_course__tno__mcno__semester=semester)
    for element in rows_in_exam:
        if Students_id.get(element.sno.username) == None:
            stu = Students(element.sno.username, element.sno.name,
                           element.sno.in_cls.major.major.mno, element.sno.in_year, element.sno.in_cls.name)
            stu.examSchedule = String_to_examTable(element.time)
            Students_id[element.sno.username] = stu
        else:
            Students_id[element.sno.username].examSchedule = mergeTable(Students_id[element.sno.username].examSchedule,String_to_examTable(element.time))
        if Classrooms_id.get(element.where) == None:
            room = Classroom(element.where.crno, element.where.crtype, element.where.contain_num)
            room.examSchedule = String_to_examTable(element.time)
            Classrooms_id[element.where.crno] = room
        else:
            Classrooms_id[element.where].examSchedule = mergeTable(Classrooms_id[element.where].examSchedule, String_to_examTable(element.time))

def exam_time_generate(bf: Buffer):
    for i in range(7):
        for j in range(5):
            if bf.examSchedule[i][j] != '':
                if j + 2 <= 4:
                    j += 2
                elif j + 2 >= 5:
                    break
            else:
                return str(i)+'-'+str(j)


def exam_schedule():
    init()
    init_exam()
    for e in Classrooms_id:
        Classrooms_id[e].cmp_type = 1
    heap_bigroom = []
    heap_midroom = []
    heap_smallroom = []
    room_set = ClassRoom.objects.all()
    for elements in room_set:
        if Classrooms_id.get(elements.crno) == None:
            Classrooms_id[elements.crno] = Classroom(elements.crno, elements.crtype, elements.contain_num)
        if Classrooms_id[elements.crno].type == '大':
            heapq.heappush(heap_bigroom, Classrooms_id[elements.crno])
        if Classrooms_id[elements.crno].type == '中':
            heapq.heappush(heap_midroom, Classrooms_id[elements.crno])
        if Classrooms_id[elements.crno].type == '小':
            heapq.heappush(heap_smallroom, Classrooms_id[elements.crno])
    exam_set = Teacher_Schedule_result.objects.filter(tno__mcno__year=year, tno__mcno__semester=semester)
    for course in exam_set:
        if '必修' in course.tno.mcno.cno.course_type:
            if course.current_number >= 165:  # 三个大教室
                target_cnt = int(course.current_number / 3)
                cnt_room = 0
                students_set = Schedule_result.objects.filter(tno=course.tno, time=course.time, where=course.where)
                bf = Buffer()
                for element in students_set:
                    if target_cnt - 1 < 0:
                        # 分配时间、地点判断生成的时间冲突
                        room = heap_bigroom[0]
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.examSchedule = mergeTable(room.examSchedule, bf.examSchedule)
                        bf.classrooms.append(room)
                        res = exam_time_generate(bf)
                        exam_write_to_database(bf, course, res)
                        room.exam_time_count += 1
                        heapq.heapify(heap_bigroom)
                        bf = Buffer()
                        if cnt_room + 1 == 3:
                            cnt_room += 1
                            target_cnt = course.current_number - int(course.current_number / 3) * 2
                        else:
                            target_cnt = int(course.current_number / 3)
                    else:
                        target_cnt -= 1
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.students.append(element.sno.username)

            elif course.current_number < 165 and course.current_number >= 100: #两个大教室
                target_cnt = int(course.current_number / 2)
                cnt_room = 0
                students_set = Schedule_result.objects.filter(tno=course.tno, time=course.time, where=course.where)
                bf = Buffer()
                for element in students_set:
                    if target_cnt - 1 < 0:
                        # 分配时间、地点判断生成的时间冲突
                        room = heap_bigroom[0]
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.examSchedule = mergeTable(room.examSchedule, bf.examSchedule)
                        bf.classrooms.append(room)
                        res = exam_time_generate(bf)
                        exam_write_to_database(bf, course, res)
                        room.exam_time_count += 1
                        heapq.heapify(heap_bigroom)
                        bf = Buffer()
                        if cnt_room + 1 == 2:
                            cnt_room += 1
                            target_cnt = course.current_number - int(course.current_number / 2)
                        else:
                            target_cnt = int(course.current_number / 2)
                    else:
                        target_cnt -= 1
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.students.append(element.sno.username)
            elif course.current_number < 100 and course.current_number >= 80: #两个中教室
                target_cnt = int(course.current_number / 2)
                cnt_room = 0
                students_set = Schedule_result.objects.filter(tno=course.tno, time=course.time, where=course.where)
                bf = Buffer()
                for element in students_set:
                    if target_cnt - 1 < 0:
                        # 分配时间、地点判断生成的时间冲突
                        room = heap_midroom[0]
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.examSchedule = mergeTable(room.examSchedule, bf.examSchedule)
                        bf.classrooms.append(room)
                        res = exam_time_generate(bf)
                        exam_write_to_database(bf, course, res)
                        room.exam_time_count += 1
                        heapq.heapify(heap_midroom)
                        bf = Buffer()
                        if cnt_room + 1 == 2:
                            cnt_room += 1
                            target_cnt = course.current_number - int(course.current_number / 2)
                        else:
                            target_cnt = int(course.current_number / 2)
                    else:
                        target_cnt -= 1
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.students.append(element.sno.username)
            elif course.current_number < 80 and course.current_number >= 25:  #一个中教室
                target_cnt = course.current_number
                students_set = Schedule_result.objects.filter(tno=course.tno, time=course.time, where=course.where)
                bf = Buffer()
                for element in students_set:
                    if target_cnt - 1 < 0:
                        # 分配时间、地点判断生成的时间冲突
                        room = heap_midroom[0]
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.examSchedule = mergeTable(room.examSchedule, bf.examSchedule)
                        bf.classrooms.append(room)
                        res = exam_time_generate(bf)
                        exam_write_to_database(bf, course, res)
                        room.exam_time_count += 1
                        heapq.heapify(heap_midroom)
                    else:
                        target_cnt -= 1
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.students.append(element.sno.username)
            elif course.current_number <= 25:  # 一个小教室
                target_cnt = course.current_number
                students_set = Schedule_result.objects.filter(tno=course.tno, time=course.time, where=course.where)
                bf = Buffer()
                for element in students_set:
                    if target_cnt - 1 < 0:
                        # 分配时间、地点判断生成的时间冲突
                        room = heap_smallroom[0]
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.examSchedule = mergeTable(room.examSchedule, bf.examSchedule)
                        bf.classrooms.append(room)
                        res = exam_time_generate(bf)
                        exam_write_to_database(bf, course, res)
                        room.exam_time_count += 1
                        heapq.heapify(heap_smallroom)
                    else:
                        target_cnt -= 1
                        bf.examSchedule = mergeTable(bf.examSchedule, Students_id[element.sno.username].examSchedule)
                        bf.students.append(element.sno.username)

def exam_write_to_database(bf:Buffer, course, res:str):
    for element in bf.students:
        row = Exam_Schedule.objects.create(
            sno=Student.objects.get(username=element),
            tno_mno_course=course,
            time=res,
            where=ClassRoom.objects.get(crno=bf.classrooms[0].id)
        )
        row.save()
        Students_id.get(element).examSchedule[int(res.split('-')[0])][int(res.split('-')[1])] = '20-20'


# 查询考试时间view里
def search_exam_time(stu_username: str):
    pass


if __name__ == '__main__':
    pass
    #autoSchedule()
    #exam_schedule()
