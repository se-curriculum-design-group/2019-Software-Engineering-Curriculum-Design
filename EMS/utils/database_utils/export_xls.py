import pandas as pd
import xlrd, xlsxwriter
from backstage.models import Student, Teacher, AdmClass, MajorPlan, Major

def export_Student(in_year=None ,in_class='', major=''):
    # 创建一个excel
    workbook = xlsxwriter.Workbook("stu.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet("stu")
    # worksheet = workbook.add_worksheet("bug_analysis")
    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})
    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    headings = ['学生号', '姓名', '性别', '年级', '班级', '专业', '已修学分']
    data = [[],  [],  [],  [],  [],  [],  []]
    stu_
    # 写入表头
    worksheet.write_row('A1', headings, bold)
    # 写入数据
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    worksheet.write_column('E2', data[4])
    worksheet.write_column('F2', data[5])
    worksheet.write_column('G2', data[6])

