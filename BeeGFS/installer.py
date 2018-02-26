# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os
import sys
import platform

def main():
    if os.getuid()!=0:
        print ('Requires root privileges!')
        sys.exit('Exiting Installer')
    if len(sys.argv)==2:
        if sys.argv[1]=='mgmt':
            os.system('python ./BeeGFS/src/management_install.py')
        elif sys.argv[1]=='meta':
            os.system('python ./BeeGFS/src/metadata_install.py')
        elif sys.argv[1]=='client':
            os.system('python ./BeeGFS/src/client_install.py')
        elif sys.argv[1]=='storage':
            os.system('python ./BeeGFS/src/storage_install.py')
        elif sys.argv[1]=='admon':
            os.system('python ./BeeGFS/src/admon_install.py')
        elif sys.argv[1]=='-h':
            usage()
    else:
        usage()
        sys.exit('No parameter provide, Exiting the Installer')

    if (platform.dist()[0]=='centos'):
        print ('Installing the required packages.please waiting......\n')
        os.system('''
        yum update -y
        yum install -y vim curl git wget ntp gcc libaio* librbd* mdadm java 
        ''')
    elif (platform.dist()[0]=='Ubuntu'):
        print ('Installing the required packages.please waiting......\n')
        os.system('''
        apt-get update -y
        apt-get install -y vim curl git wget ntp gcc libaio* librbd* mdadm java
        ''')
    else:
        print('Operating System not supported')
        sys.exit('Exiting Installer')


def usage():
    print ('''
    usage: installer.py [-h] [parameter]
    positional arguments:
        mgmt    install the management service
        client  install the client service
        meta    install the metadata service
        storage install the storage service
        admon   install the GUI service
    ''')
main()



