# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'


import os,commands,time
from Helper import Helper
Helper = Helper()

def get_file():
    file_dir = os.getcwd()+'/orcafs-packages'
    file_list=[]
    cmd_list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if 'debuginfo' in os.path.splitext(file)[0]:
                files.remove(file)
                continue
        for file in files:
            if os.path.splitext(file)[1] == '.rpm':
                file_list.append(file)
                cmd_list.append('rpm -i ' + os.path.join(root, file))
    install_rpm(cmd_list)


def install_rpm(cmd_list):
    host_info = Helper.get_hostinfo()

    cmd_list1=[]
    hostname = commands.getoutput('hostname')
    print hostname
    for key in host_info.keys():
        if hostname==host_info[key][1]:
            if key == 'Client':
                cmd_list1 = [cmd for cmd in cmd_list if 'client' in cmd or 'admon' in cmd or 'common' in cmd or 'helperd' in cmd or 'utils' in cmd or 'opentk' in cmd]
            elif key == 'Storage':
                cmd_list1 = [cmd for cmd in cmd_list if 'storage' in cmd or 'common' in cmd or 'opentk' in cmd]
            elif key == 'Metadata':
                cmd_list1 = [cmd for cmd in cmd_list if 'meta' in cmd or 'common' in cmd or 'opentk' in cmd]
            elif key == 'Management':
                cmd_list1 = [cmd for cmd in cmd_list if 'mgmtd' in cmd or 'common' in cmd or 'opentk' in cmd]
            else:
                print 'No packages matched.'
    print cmd_list1
    exe_cmd(cmd_list1)

def exe_cmd(cmd):
    for m in cmd:
        if 'opentk' in cmd:
            print 'Current CMD is:', m
            stdout= commands.getoutput(m)
            if 'error' in stdout:
                print 'stderr:', stdout
            else:
                print 'Package installed.'
            cmd.remove(m)
    for m in cmd:
        print 'Current CMD is:', m
        stdout = commands.getoutput(m)
        if 'already installed' in stdout:
            print 'stdout:', stdout.lstrip()
        elif 'error' in stdout:
            print 'stderr:',stdout
        else:
            print 'Package installed.'

if __name__=='__main__':
    print 'Now Starting to install the rpm packages remotely.'
    get_file()


