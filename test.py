#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
name = ['physics', 'chemistry', 1997, 2000,1, 2, 3, 4, 5, 6, 7,2,4,5,19,1, 2, 3, 4, 5, 6, 7]
first_pos = 0

for i in range(name.count(2)):
    new_list = name[first_pos:]

    next_pos = new_list.index(2) +1
    print "Find:", first_pos+next_pos
    first_pos += next_pos
    
for i in range(len(name)):
    if name[i] ==2:
        print i+1
pos = 0        
for i in range(name.count(2)):
    if first_pos==0:
        pos = name.index(2) +1
    else:
        pos = name.index(2,pos+1 )
    print pos +1
'''
'''
keys = []
value =[]
import re
with open ('D:/Eclipse/Workspace/PythonCase/test.txt','r') as f:
        for line in f:
                res = re.match(r'(.+):\s+(\d+)',line.strip())
                print res.group(1)
                keys.append(res.group(1))
                value.append(res.group(2))
        print keys    
'''
'''
#res = re.match(r'(\w+):\s+(\d+)','Cached:          5021652 kB')
#print res.group(2)
'''


def pa():
    x = 0
    def b():
        x=2
        def c():
            x=3
            print x
        c()
    b()
pa()

a ='这个歌'
print a.decode('utf-8')

import os
import hashlib
# res = os.popen('dir').read()
# print type(res)
# print res.decode('gbk')

hash = hashlib.md5()
hash.update('name')
hash.update('hx')
print hash.hexdigest()


print os.path.dirname(__file__)
import getpass
user = getpass.getuser()
print user
# passwd = getpass.getpass()
# print passwd

msg = 'get ls dir'
list = msg.split(' ')
print list
ins = "lst_file|%s"%(' '.join(list[1:]))
print ins


def help(self):
    print '''
    command_type    command_instruction
    help            help
    get             get remote_filename
    put             put local_filename
    exit            exit the system
    ls              list all the files int the current directory
    del             del the remote filename
    cd              cd  the dest_dir
    '''

print os.path.dirname(__file__)