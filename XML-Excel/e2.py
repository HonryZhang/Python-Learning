# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import xml.dom.minidom
import xlwt
file=xlwt.Workbook(encoding='ascii')
table=file.add_sheet('test',cell_overwrite_ok=True)
dom = xml.dom.minidom.parse('disk-testsuite-deep.xml')
root=dom.documentElement
itemlist = root.getElementsByTagName('testcase')
plist = root.getElementsByTagName('preconditions')
actions = root.getElementsByTagName('actions')
exs = root.getElementsByTagName('expectedresults')
item=itemlist[0]
un=item.getAttribute("name")
print un
for i in range(0,len(itemlist)):
    item=itemlist[i]
    pp=plist[i]
    un=item.getAttribute("name")
    table.write(i,0,un)
    try:
        action=actions[i]
        ex=exs[i]
    except IndexError,e:
        continue
    if pp.firstChild==None:
        continue
    if ex.firstChild==None:
        continue
    else:
        table.write(i,1,pp.firstChild.data)
        table.write(i,2,action.firstChild.data)
        table.write(i,3,ex.firstChild.data)
file.save('mytest.xls')
print "over"