#!/usr/bin/python
#-*- coding:utf-8 -*-
#删除井号开头的行以及空行
'''
import os
import re
if (os.path.exists('beegfs-client.conf')):
	os.system ('rm beegfs-client.conf')
if (os.path.exists('beegfs-client.conf.bak')):
	print "Bak File exist"
	os.system('cp beegfs-client.conf.bak beegfs-client.conf')
#else:
#	os.system('cp beegfs-client.conf beegfs-client.conf.bak')

with open ('beegfs-client.conf','r') as f:
	lines = f.readlines()
with open ('beegfs-client.conf','w') as f_w:
	for line in lines:
		s = re.match("^#\s",line)
		if s:
			continue;
#		f_w.write(line)
		data = line.strip()
		if len(data)!=0:
			f_w.write(data)
			f_w.write('\n')
'''

total = 0
blank = 0
pound = 0

with open ('beegfs-client.conf','r') as f:
	lines = f.readlines()
	for line in lines:
		total +=1
		if not line.split():
			blank +=1
		line.strip()
		if line.startswith('#'):
			pound +=1
	print 'Total line:',total
	print 'Total blank',blank
	print 'Total pound',pound
