# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import xlwt,re
import xml.etree.ElementTree as ET

class xml_excel():
    def __init__(self):
        self.file = xlwt.Workbook(encoding='utf-8')
        self.borders = xlwt.Borders()
        self.pattern = xlwt.Pattern()
        self.font = xlwt.Font()
        self.style = xlwt.XFStyle()

    def sheet_border(self):
        self.borders.left = xlwt.Borders.THIN
        self.borders.right = xlwt.Borders.THIN
        self.borders.top = xlwt.Borders.THIN
        self.borders.bottom = xlwt.Borders.THIN
        self.style.borders = self.borders

        return self.style

    def write_head(self,name1):
        self.add_sheet = self.file.add_sheet(name1,cell_overwrite_ok=True)
        self.add_sheet.write(0,0,'用例模块',self.sheet_border())
        self.add_sheet.write(0,1,'用例标题',self.sheet_border())
        self.add_sheet.write(0, 2, '用例概要', self.sheet_border())
        self.add_sheet.write(0, 3, '前提条件', self.sheet_border())
        self.add_sheet.write(0, 4, '编号', self.sheet_border())
        self.add_sheet.write(0, 5, '操作步骤', self.sheet_border())
        self.add_sheet.write(0, 6, '预期结果', self.sheet_border())

    def write_count(self,num1,num2,str1):
        self.add_sheet.write(num1,num2,str1,self.sheet_border())

    def excel_merge(self,num11,num22,num33,num44,str11):
        self.add_sheet.write_merge(num11,num22,num33,num44,str11,self.sheet_border())

    def cell_width(self):
        self.add_sheet.col(0).width = 5000
        self.add_sheet.col(1).width = 10000
        self.add_sheet.col(2).width = 5000
        self.add_sheet.col(3).width = 10000
        self.add_sheet.col(5).width = 20000
        self.add_sheet.col(5).height = 5000
        self.add_sheet.col(6).width = 40000
        self.add_sheet.col(6).height = 5000

    def save_excel(self):
        self.file.save(('testcase-all.xls'))

    def excel_replace(self,ss):
        self.re_cdata = re.compile(' ]*>',re.I)
        self.s = re.compile((r'&;'))
        # &; 符号
        self.re_ca = re.compile(r'&;')
        # 小于号
        self.re_cx = re.compile(r'<')
        # 大于号
        self.re_cd = re.compile(r'>')
        # 双引号
        self.re_cs = re.compile(r'"')
        # 空格
        self.re_ck = re.compile(r'')
        # 破折号
        self.re_cp = re.compile(r'—')
        # 上尖括号;
        self.re_cj = re.compile(r'…')
        # 中文双引号
        self.re_czsl = re.compile(r'“')
        # 中文双引号
        self.re_czsr = re.compile(r'”')
        # 中文单引号
        self.re_czdl = re.compile(r'‘')
        # 中文单引号
        self.re_czdr = re.compile(r'’')
        s = self.re_cdata.sub('', ss)
        s = self.re_ca.sub(r'&;', s)
        s = self.re_cx.sub(r'<', s)
        s = self.re_cd.sub(r'>', s)
        s = self.re_cs.sub(r'"', s)
        s = self.re_ck.sub(r' ', s)
        s = self.re_cp.sub(r'-', s)
        s = self.re_cj.sub(r'^', s)
        s = self.re_czsl.sub(r'“', s)
        s = self.re_czsr.sub(r'”', s)
        s = self.re_czdl.sub(r'‘', s)
        s = self.re_czdr.sub(r'’', s)
        return s

    def replace_str(self,str):
        res = str.replace('<p>','').replace('</p>','').replace('<br />','').replace('<br/>','').replace('<div>','').replace('</div>','').replace('</span>','')
        #print res
        return res

tree = ET.parse("/Users/hongrui/PycharmProjects/Orcadt/Python-Learning/XML-Excel/Functional_cases.xml")
# 获取 xml 根目录
root = tree.getroot()
# 获取 测试用例集
testsuite_per = root.findall('testsuite')
# 循环测试用例集
aa = {}
dict_temp = {}
xe = xml_excel()
for num_suite in range(0, len(testsuite_per)):
    xe.write_head(testsuite_per[num_suite].get('name'))
    #print testsuite_per[num_suite].get('name').encode('utf-8')
    row_flag = 1
    flag = row_flag
    list_row = [0]
    #print testsuite_per[num_suite]
    for testsuite_son in testsuite_per[num_suite].findall('testsuite'):
        testcase = testsuite_son.getiterator('testcase')
        num = len(testcase)

        for case in range(0,num):
            steps = testcase[case].getiterator('step')
            for step in steps:
                list_temp=[]
                list_temp.append(step[1].text)

                list_temp.append(step[2].text)

                dict_temp[step[0].text]= list_temp

            row_start = row_flag
            if len(steps)!=0:
                for i in range(1,len(steps)+1):
                    xe.write_count(row_flag,4,str(i))
                    if dict_temp[str(i)][0]is not None:
                        #print dict_temp[str(i)][0]
                        #xe.write_count(row_flag,5,xe.excel_replace(dict_temp[str(i)][0]))
                        xe.write_count(row_flag,5,xe.replace_str(dict_temp[str(i)][0]))
                    else:
                        xe.write_count(row_flag,5,dict_temp[str(i)][0])
                    if dict_temp[str(i)][1] is not None:
                        #print dict_temp[str(i)][1]
                        #xe.write_count(row_flag, 6, xe.excel_replace(dict_temp[str(i)][1]))
                        xe.write_count(row_flag, 6, xe.replace_str(dict_temp[str(i)][1]))
                    else:
                        xe.write_count(row_flag, 6, dict_temp[str(i)][1])
                    row_flag+=1
                    #print row_flag
            else:
                row_flag+=1
                continue

            if testcase[case].get('name') is not None:
                #print testcase[case].get('name')
                xe.excel_merge(row_start,row_flag-1,1,1,xe.replace_str(testcase[case].get('name')))

            if testcase[case].find('summary').text is not None:
                summary = xe.replace_str(testcase[case].find('summary').text)
                if '<img' in testcase[case].find('summary').text:
                    pattern = '<img.+>'
                    res1 = re.sub(pattern, '', summary)
                #xe.excel_merge(row_start, row_flag - 1, 2, 2, xe.excel_replace(testcase[case].find('summary').text))
                    #xe.excel_merge(row_start,row_flag-1,2,2,xe.replace_str(testcase[case].find('summary').text))
                    xe.excel_merge(row_start, row_flag - 1, 2, 2, res1)
                else:
                    xe.excel_merge(row_start, row_flag - 1, 2, 2, summary)
            else:
                xe.excel_merge(row_start, row_flag - 1, 2, 2, testcase[case].find('summary').text)

            if testcase[case].find('preconditions').text is not None:
                precondition = xe.replace_str(testcase[case].find('preconditions').text)
                #precondition = precondition.replace('\n\t','')
                #xe.excel_merge(row_start, row_flag - 1, 3, 3, xe.replace_str(testcase[case].find('preconditions').text))
                if '<div'in testcase[case].find('preconditions').text:
                    pattern2 = '<div.+">'
                    res2 = re.sub(pattern2, '', precondition)
                    xe.excel_merge(row_start, row_flag - 1, 3, 3, res2)
                    #xe.excel_merge(row_start, row_flag - 1, 3, 3, xe.replace_str(testcase[case].find('preconditions').text))
                elif '<span' in testcase[case].find('preconditions').text:
                    pattern3 = '<span.+">'
                    res3 = re.sub(pattern3, '', precondition)
                    xe.excel_merge(row_start, row_flag - 1, 3, 3,res3)
                else:
                    xe.excel_merge(row_start, row_flag - 1, 3, 3, precondition)
            else:
                xe.excel_merge(row_start, row_flag - 1, 3, 3, testcase[case].find('preconditions').text)
            list_row.append(row_flag - 1)
        if num != 0:
            #xe.excel_merge(list_row[len(list_row) - (num+1)] + 1, list_row[len(list_row) - 1], 0, 0,testsuite_son.get('name'))
            xe.excel_merge(flag, row_flag-1, 0, 0,testsuite_son.get('name'))
            flag=row_flag
        else:
            continue
xe.cell_width()
xe.save_excel()