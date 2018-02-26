# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os,platform,sys

from Helper import Helper
import management_install

Helper = Helper()

def main():
    options = gather_info(get_defaults())
    Helper.prepare()

    install_metadata(options)

def get_defaults():
    return {
        'metadata_service_id':'2'
    }

def gather_info(defautlts):
    options={}
    options['metadata_hostname']=Helper.get_hostname()
    options['metada_hostip']=Helper.get_hostip()
    options['mgmt_hostname']=management_install.get_mgmt_info()['management_hostname']
    options['mgmt_hostip']=management_install.get_mgmt_info()['management_hostip']
    options['metadata_service_id']='2'
    return options

def install_metadata(options):
    if (platform.dist()[0] == 'centos'):
        os.system('''
            yum install -y beegfs-meta
            ''')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('''
            apt-get install -y beegfs-meta
            ''')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')

    os.system('''
    /opt/beegfs/sbin/beegfs-setup-meta -p /data/beegfs/beegfs-meta/ -s '''+ options['metadata_service_id'] + ' -m ' + options['mgmt_hostname']+'''
    /etc/init.d/beegfs-meta start
    /etc/init.d/beegfs-meta status   
    ''')

main()

