# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os,sys
import platform

from Helper import Helper
Helper = Helper()

def main():
    Helper.prepare()
    get_mgmt_info()

def install_management():
    if (platform.dist()[0]== 'centos'):
        os.system('yum install -y beegfs-mgmtd')
    elif (platform.dist()[0]=='Ubuntu'):
        os.system('apt-get install -y beegfs-mgmtd')
    else:
        print ('Operation System not supported')
        sys.exit('Exiting the Installer')

    os.system('''
    /opt/beegfs/sbin/beegfs-setup-mgmtd -p /data/beegfs/beegfs_mgmtd
    /etc/init.d/beegfs-mgmtd start
    /etc/init.d/beegfs-mgmtd status
    ''')
def get_mgmt_info():
    mgmt_info = {}
    mgmt_info['management_hostname']=Helper.get_hostname()
    mgmt_info['management_hostip']=Helper.get_hostip()
    return  mgmt_info

main()


