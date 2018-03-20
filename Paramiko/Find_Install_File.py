# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'


import os

def filename(fir_dir):
    cmd_list=[]
    file_list = []
    for root,dirs,files in os.walk(fir_dir):
        # print root,
        # print dirs,

        # print files
        for file in files:
            if 'debuginfo' in os.path.splitext(file)[0]:
                files.remove(file)
                continue
        for file in files:
            if os.path.splitext(file)[1] == '.rpm':
                file_list.append(file)
                cmd_list.append('rpm -i '+os.path.join(root, file))
    # print file_list
    # print len(cmd_list),len(cmd_list)
    cmd_list1=cmd_list2=cmd_list3=cmd_list4=[]
    role = raw_input('hostname:')
    for cmd in cmd_list:
        if role=='Client':
#            ip1 = host_info[key][0]
            cmd_list1 = [cmd for cmd in cmd_list if 'client' in cmd or 'admon' in cmd or 'common'in cmd or 'helperd' in cmd or'utils' in cmd or 'opentk' in cmd]
#            if 'client' in cmd or 'admon' in cmd or 'common'in cmd or 'helperd' in cmd or'utils' in cmd:
#               cmd_list1.append(cmd)
 #           print 'Client:', cmd_list1,len(cmd_list1)
        elif role=='Storage':
            cmd_list2 = [cmd for cmd in cmd_list if 'storage' in cmd or 'common' in cmd]
        elif role =='Metatada':
            cmd_list3 = [cmd for cmd in cmd_list if 'meta' in cmd or 'common' in cmd]
        elif role=='Management':
            cmd_list4 = [cmd for cmd in cmd_list if 'mgmtd' in cmd or 'common' in cmd]
        else:
            print 'no cmmdn'

    print 'Client:', cmd_list1,len(cmd_list1)
#    print 'IP1:',ip1
    # print 'Storage:', cmd_list2,len(cmd_list2)
    # print 'Metadata:', cmd_list3,len(cmd_list3)
    # print 'Management:', cmd_list4,len(cmd_list4)

#file_dir = raw_input('file path:')
file_dir = '/Users/hongrui/PycharmProjects/Orcadt/Python-Learning/Paramiko'
filename(file_dir)

#ftp_path = str(raw_input('Input the whole and correct ftp link address:'))
#cmd_str = 'wget -nH -m --ftp-user=swint --ftp-password=swint ' + " '%s' " % ftp_path
#print cmd_str