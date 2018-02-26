#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import xml.etree.cElementTree as ET
import xml.dom.minidom as xx
import os,xlwt, datetime

workbook = xlwt.Workbook(encoding='utf-8')

booksheet = workbook.add_sheet(u'sheet_1')
booksheet.col(0).width = 5120
booksheet.col(1).width = 5120
booksheet.col(2).width= 5120
booksheet.col(3).width= 5120
booksheet.col(4).width= 5120
booksheet.col(5).width= 5120

dom = xx.parse(r'C:\\Users\Hongrui\Downloads\excel2xml\test.xml')
root = dom.documentElement
row = 1
col = 1

borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1

style = xlwt.easyxf('align:wrap on,vert centre, horiz center')

title = xlwt.easyxf(u'font:name 仿宋,height 240 ,colour_index black, bold on, italic off; align: wrap on, vert centre, horiz center;pattern: pattern solid, fore_colour light_orange;')

item = '测试项'
Subitem = '测试分项'
CaseTitle = '测试用例'
Condition = '前置条件'
actions = '操作步骤'
Result = '预期结果'

booksheet.write(0,0,item,title)
booksheet.write(0,1,Subitem,title)
booksheet.write(0,2,CaseTitle,title)
booksheet.write(0,3,Condition,title)
booksheet.write(0,4,actions,title)
booksheet.write(0,5,Result,title)

booksheet.panes_frozen = True
booksheet.horz_split_pos = 1

print root.childNodes
for i in root.childNodes:
    testsuite = i.getAttribute('name'.strip())
    print testsuite
    print 'row is:',row

    booksheet.write(row,col,testsuite,style)

    for dd in i.childNodes:
        print ' %s  '%dd.getAttribute('name'.strip())
        testsuite2 = dd.getAttribute('name')
        print testsuite2
        if not dd.getElementsByTagName('testcase'):
            print 'testcase is :%s'%testsuite2
            row+=1
            booksheet.write(row,2, testsuite2,style)
        row+=1

        booksheet.write(row,1,testsuite2,style)

        itemlist = dd.getElementsByTagName('testcase')
        for subb in itemlist:
            testcase = subb.getAttribute('name')
            row+=1

            booksheet.write(row, 2, testcase,style)

            ilist = subb.getElementsByTagName('preconditions')
            for ii in ilist:
                preconditions = ii.firstChild.data.replace("<br />"," ")
                col+=1
                booksheet.write(row,3,preconditions,style)

            steplist = subb.getElementsByTagName('actions')
            for step in steplist:
                actions = step.firstChild.data.replace("<br />"," ")
                col += 1
                booksheet.write(row, 4, actions, style)

            expectlist = subb.getElementsByTagName('expectedresults')

            for expect in expectlist:
                result = expect.childNodes[0].nodeValue.replace("<br />", "")
                booksheet.write(row, 5, result, style)
        row+=1

    workbook.save('demo.xls')



