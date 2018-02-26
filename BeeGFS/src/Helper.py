# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os,socket
import sys,commands
import platform

class Helper:
    def prepare(self):
        if (platform.dist()[0]=='centos'):
            os.system('''
            yum clean all
            yum update -y
            ''')
            if (platform.dist()[0]+ platform.dist()[1][0] =='centos7'):
                os.system('''
                sudo wget -O /etc/yum.repos.d/beegfs-rhel7.repo http://www.beegfs.io/release/beegfs_6/dists/beegfs-rhel7.repo
                ''')
            elif (platform.dist()[0]=='Ubuntu'):
                os.system(
                    'curl -Lo /etc/apt/sources.list.d/beegfs-deb8.list http://www.beegfs.com/release/beegfs_6/dists/beegfs-deb8.list')
                os.system('curl -L http://www.beegfs.com/release/latest-stable/gpg/DEB-GPG-KEY-beegfs | apt-key add -')
                os.system('apt-get update -y')
            else:
                print ('Operation System not supported')
                sys.exit('Exiting the Installer')

    def get_hostname(self):
        hostname = str(socket.gethostname())
        print 'Name of current server:',hostname
        return hostname


    def get_hostip(self):
        pcname = socket.gethostname()
        hostip = socket.gethostbyname(pcname)
        print 'IP address of current server:',hostip
        return hostip


    def default_prompt(self,parameter,default_value):
        response = raw_input(parameter+'('+default_value+')'":")
        if response:
            return response
        else:
            return default_value


    def find_replace(self,file_path,find,replace):
        file_data = None
        with open(file_path,'r') as f:
            file_data = f.read()
            file_data = file_data.replace(find,replace)
        with open (file_path,'w')as f:
            f.write(file_data)

    def get_disk(self):
        nvme_disk_count = int(commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'nvme' |wc -l'''))
        hdd_disk_count = int(commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'sd' |wc -l'''))
        nvme_disk_list = commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'nvme' ''')
        hdd_disk_list = commands.getoutput('''lsblk -nd | awk '{print "/dev/"$1}' |grep -E 'sd' ''')
        if nvme_disk_count==0:
            print 'No nvme device found. Checking HDD device now.'
            if hdd_disk_count==0:
                print 'No HDD device found yet. Exiting...'
                sys.exit()
            else:
                return nvme_disk_list.split('\n')
        else:
            return hdd_disk_list.split('\n')


    def check_disk(self):


