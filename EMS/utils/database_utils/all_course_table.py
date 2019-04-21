import pandas as pd
import os
from random import randint, choice, choices
from backstage.models import Student, Major, College, MajorPlan, Teacher, AdmClass, ClassRoom
from scoreManagement.models import Course, MajorCourses, Teaching


base_dir = '../others/'
xls_file = os.listdir(base_dir)
print(xls_file)

item_list = []
data_frames = []


for xls_name in xls_file:
    xls_path = os.path.join(base_dir, xls_name)
    data_frame = pd.read_excel(xls_path)
    data_frames.append(data_frame)

for item in data_frames[0]:
    item_list.append(item)

print(len(item_list))


# def init_all_course_table():
#     for data_frame in data_frames:
#         for state, cno, cname, score, exam_method, course_type,\
#             teachers, teach_class_name, week_duration,\
#             class_time, class_location, college, adm_classes, year, semester in zip(
#           data_frame[item_list[0]], data_frame[item_list[1]], data_frame[item_list[2]], data_frame[item_list[3]],\
#           data_frame[item_list[4]], data_frame[item_list[5]], data_frame[item_list[6]], data_frame[item_list[7]],\
#           data_frame[item_list[8]], data_frame[item_list[9]], data_frame[item_list[10]], data_frame[item_list[11]],\
#           data_frame[item_list[12]], data_frame[item_list[13]], data_frame[item_list[14]]
#         ):
#             print(state, cno, cname, score, exam_method, course_type,\
#             teachers, teach_class_name, week_duration,\
#             class_time, class_location, college, adm_classes, year, semester)
#             try:
#                 table_item = AllCourseTable.objects.create(
#                     state= state=='开课',
#                     cno=cno,
#                     cname=cname,
#                     score=score,
#                     exam_method=True,
#                     course_type=course_type,
#                     teachers=teachers,
#                     teach_class_name=teach_class_name,
#                     week_duration=week_duration,
#                     class_time=class_time,
#                     class_location=class_location,
#                     college=college,
#                     adm_classes=adm_classes,
#                     year=year,
#                     semester=semester
#                 )
#                 table_item.save()
#                 print("success %d"%(len(AllCourseTable.objects.all())))
#             except:
#                 print("Error: number: %d"%(len(AllCourseTable.objects.all())))
#     pass


if __name__ == '__main__':
    # init_all_course_table()
    pass