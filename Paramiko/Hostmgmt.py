# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import paramiko,re,os,sys,time
import threading
from Helper import Helper
Helper = Helper()
# host_info={}
# host_credential={}
username = Helper.get_credential()['username']
passwd = Helper.get_credential()['password']
host_info = Helper.get_hostinfo()


def thread_run(cmd):
    # username  = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    # host_info = Helper.get_hostinfo()

    threads=[]
    print 'Now Begining......'
    for v in host_info.values():
        print 'ip address:',v[0]
        ip = v[0]
        t = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
#    print 'All Command Executed......\n'


# def execute_configure_cmd(ip,cmd):
#
#     print 'Now Begin to install RPMs\n'
#     ssh2(ip,username,passwd,cmd)
#     print 'All Command Executed......\n'


def install_basic():
    # username = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    # host_info = Helper.get_hostinfo()
    cmd_basic = [
        'sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak',
        'sudo curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo',
        'sudo yum install -y vim wget ntp',
        'sudo sed -i \'s/#PermitRootLogin yes/PermitRootLogin yes/\' /etc/ssh/sshd_config',
        'yum clean all',
        'yum makecache',
        'yum -y update',
        'sudo yum install -y mdadm libuuid-devel libibverbs-devel librdmacm-devel libattr-devel redhat-rpm-config',
        'sudo yum install -y rpm-build xfsprogs-devel cppunit cppunit-devel zlib-devel openssl-devel sqlite',
        'sudo yum install -y sqlite-devel ant gcc-c++ gcc redhat-lsb-core java-devel',
        'sudo service sshd restart',
        'sudo service ntpd restart',
        'systemctl stop firewalld.service',
        'systemctl disable firewalld.service'
    ]
    cmd_client = [
        'sudo yum update -y',
        'sudo yum install -y kernel-devel-$(uname -r)',
        'sudo sed -i \'s/SELINUX=enforcing/SELINUX=disabled/\' /etc/selinux/config',
        'sudo yum install -y gcc git libaio* librbd*',
        'sudo rm -rf fio/',
        'git clone git://git.kernel.dk/fio.git',
        'cd fio && ./configure && make && make install'
    ]
    # host_info = Helper.get_hostinfo()
    exit_flag = False
    for key in host_info.keys():
        #ip = host_info[key][0]
        if key=='Client':
            ip = host_info[key][0]
            #cmd = cmd_basic+cmd_client
            if(ssh2(ip, username, passwd, cmd_client)):
                exit_flag=True
        else:
            thread_run(cmd_basic)
            exit_flag=True
            break
    return exit_flag
            #ip = host_info[key][0]
            #thread_run(cmd)
    #         if(ssh2(ip,username,passwd,cmd)):
    #             exit_flag=True
    #     else:
    #         if(ssh2(ip, username, passwd, cmd_basic)):
    #             exit_flag = True
    # return exit_flag


            #thread_run(cmd_basic)
#    return True

# def get_credential():
#     with open('credential') as f:
#         for line in f.readlines():
# #            print type(line)
#             line_list = line.rstrip().split(':')
#             host_credential[line_list[0]] = line_list[1]
#     f.close()
#     return host_credential
#
# def get_hostinfo():
#     with open('hostconfig') as f:
#         for line in f.readlines():
#             line_list = re.split(r'\s+',line.rstrip())
#             info=[line_list[1],line_list[2]]
#             host_info[line_list[0]]=info
#     f.close()
#     return host_info

def write_etc_host():
    exit_flag = False
    host_info = Helper.get_hostinfo()
    cmd_list = []
    for value in host_info.values():
        cmd = 'sudo echo '+value[0]+' '+value[1]+' |sudo tee -a /etc/hosts'
        cmd_list.append(cmd)

    for v in host_info.values():
        print 'ip address:',v[0]
        ip = v[0]
        if (ssh2(ip, username, passwd, cmd_list)):
            exit_flag = True
        else:
            exit_flag=False
    return exit_flag

    # if thread_run(cmd_list):
    #     exit_flag=True
    # else:
    #     exit_flag=False
    # return exit_flag

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            time.sleep(2)
            print 'Current CMD is:',m
            sdtin,stdout,stderr = ssh.exec_command(m,get_pty=True)
            err_list = stderr.readlines()
            if len(err_list)>0:
                #print err_list[0],
                # if '% Total    % Received' in err_list[0]:
                #     continue
                # else:
                sys.exit('\033[1;31m Error: Incorrect Command:\033[0m %s'%(m))
            else:
                print '%s:\tOK\n' %(ip)
                for out in stdout.readlines():
                    if 'Error' in out or 'ERROR' in out:
                        sys.exit('\033[1;31m Error: Failed to execute command:\033[0m %s'%(m))
                    else:
                        print out.rstrip()
        ssh.close()
        return True
    except SystemExit,value:
        print 'Connect Failed.%s:\t%s'%(ip,value)
        return False
    except Exception,e:
        print '\033[1;31mConnect Failed:\033[0m',e
        return False
    # finally:
    #     sys.exit('Connection Failed')
'''
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            print 'Current CMD is:',m
            stdin,stdout,stderr = ssh.exec_command(m)
            out = stdout.readlines()
            for o in out:
                print o.rstrip()
        print '%s:\tOK\n'%(ip)
        ssh.close()
        return True
    except:
        print '%s:\tError\n'%(ip)
        sys.exit('Connection Failed')
'''
def cluster_ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        exit_flag = False
        for m in cmd:
            print 'Current CMD is:',m
            stdin,stdout,stderr = ssh.exec_command(m)
            err_list = stderr.readlines()
            if len(err_list)>0:
                print err_list[1],
                if 'could not be found' in err_list[1]:
                    print'\033[1;31m Service is not installed or restarted\033[0m'
                    continue
                else:
                    sys.exit('\033[1;31m Error: Incorrect Command:\033[0m %s' % (m))
            else:
                print '%s:\tOK\n' %(ip)
                for out in stdout.readlines():
                    out = out.rstrip()
                    if 'Error' in out or 'ERROR' in out or 'error' in out:
                        sys.exit('\033[1;31m Error: Failed to execute command:\033[0m %s'%(m))
                    elif 'is stopped' in out:
                        print 'Instance is existed, but it\'s stopped. Starting it'
                        #exit_flag=True
                        break
                    elif 'is running' in out:
                        exit_flag=True
                        break
            if exit_flag:
                break
        ssh.close()
        return True
    except SystemExit,value:
        print '%s:\t%s'%(ip,value)
        return False
    except Exception,e:
        print '\033[1;31mError:\033[0m',e
        return False


#ftp://192.168.100.97/orcafs-packages/OrcaFS-17957644/
def rpm_Download():
    exit_flag=False
    cmd_list=[]
    ftp_path = str(raw_input('Input the whole and correct ftp link address:'))
    cmd_str = 'wget -nH -m --ftp-user=ftpUser --ftp-password=ftp ftp://192.168.100.97/orcafs-packages'+ ftp_path
    cmd_list.append(cmd_str)

    # for v in host_info.values():
    #     print 'ip address:',v[0]
    #     ip = v[0]
    #     if (ssh2(ip, username, passwd, cmd_list)):
    #         exit_flag = True
    #     else:
    #         exit_flag=False
    # return exit_flag
    thread_run(cmd_list)
    return True


def scp_to_server(ip,username,passwd,local_remote_file):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp = ssh.open_sftp()
        for k,v in local_remote_file.items():
            print k,v
            sftp.put(k,v)
        # sftp.put('Remote_install_rpm.py','/root/Remote_install_rpm.py')
        # sftp.put('hostconfig','/root/hostconfig')
        # sftp.put('Helper.py', '/root/Helper.py')
        print '%s:\tOK\n' % (ip)
        ssh.close()
        return True
    # except:
    #     print '%s:\tError\n' % (ip)
    #     sys.exit('Connection Failed')
    except Exception, e:
        print '%s:\tError\n' % (ip)
        print '\033[1;31mError:\033[0m', e
        return False

def remote_install():
    local_remote_file=dict()
    username  = Helper.get_credential()['username']
    passwd = Helper.get_credential()['password']
    host_info = Helper.get_hostinfo()
    local_remote_file['Remote_install_rpm.py']='/root/Remote_install_rpm.py'
    local_remote_file['hostconfig'] = '/root/hostconfig'
    local_remote_file['Helper.py'] = '/root/Helper.py'

    for v in host_info.values():
        print 'ip address:', v[0]
        ip = v[0]
        scp_to_server(ip,username,passwd,local_remote_file)
    cmd = ['python Remote_install_rpm.py','rm -rf Remote_install_rpm.py','rm -rf hostconfig','rm -rf Helper.py']
    thread_run(cmd)
    return True
    # else:
    #     return False


def storage_mgmt():
    host_info = Helper.get_hostinfo()
    username  = Helper.get_credential()['username']
    passwd = Helper.get_credential()['password']
    local_remote_file = {}
    local_remote_file['Helper.py'] = '/root/Helper.py'
    local_remote_file['Storage_Mgmt.py'] = '/root/Storage_Mgmt.py'

    print 'RAID Type:5> RAID5; 6> RAID6\n'

    while True:
        s_raid_type = raw_input('Select the Storage Server RAID Type <5 or 6>:')
        if int(s_raid_type) != 5 and int(s_raid_type) != 6:
            print 'No matched RAID Type, select again.\n'
        else:
            break
    s_raid_name = raw_input('Input the RAID Name <such as md0, md1..>:')
    s_disk_count = int(raw_input('Input the disk count in the RAID Group.'))

    while True:
        s_fs_type = raw_input('Select local file system type:<ext4,xfs>:')
        if s_fs_type != 'ext4' and s_fs_type != 'xfs':
            print 'No matched Filesystem Type, select again.\n'
        else:
            break

    s_mount_path = raw_input('Input the filesystem mount path:')

    for key in host_info.keys():
        if key=='Storage':
            ip = host_info[key][0]
            scp_to_server(ip,username,passwd,local_remote_file)

    cmd = ['python Storage_Mgmt.py '+str(s_raid_type)+' '+s_raid_name+' '+str(s_disk_count)+' '+s_fs_type+' '+s_mount_path,'rm -rf Storage_Mgmt.py','rm -rf Helper.py']
    for key1 in host_info.keys():
        if key1 == 'Storage':
            ip = host_info[key1][0]
            ssh2(ip, username, passwd, cmd)
            return s_mount_path

def metadata_mgmt():
    # host_info = Helper.get_hostinfo()
    # username  = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    local_remote_file = {}
    local_remote_file['Helper.py'] = '/root/Helper.py'
    local_remote_file['Metadata_Mgmt.py'] = '/root/Metadata_Mgmt.py'

    print 'RAID Type:1> RAID1; 10> RAID10\n'

    while True:
        m_raid_type = int(raw_input('Select the Metadata Server RAID Type <1 or 10>:'))
        if int(m_raid_type) != 1 and int(m_raid_type) != 10:
            print 'No matched RAID Type, select again.\n'
        else:
            break
    m_raid_name = raw_input('Input the RAID Name <such as md0, md1..>:')
    m_disk_count = int(raw_input('Input the disk count in the RAID Group.'))


    while True:
        m_fs_type = raw_input('Select local file system type:<ext4,xfs>:')
        if m_fs_type != 'ext4' and m_fs_type != 'xfs':
            print 'No matched Filesystem Type, select again.\n'
        else:
            break
    m_mount_path = raw_input('Input the filesystem mount path:')

    for key in host_info.keys():
        if key=='Metadata':
            ip = host_info[key][0]
            scp_to_server(ip,username,passwd,local_remote_file)

    cmd = ['python Metadata_Mgmt.py '+str(m_raid_type)+' '+m_raid_name+' '+str(m_disk_count)+' '+m_fs_type+' '+m_mount_path,'rm -rf Metadata_Mgmt.py','rm -rf Helper.py']
    # if thread_run(cmd):
    #     return m_mount_path
    # else:
    #     return False
    for key1 in host_info.keys():
        if key1=='Metadata':
            ip = host_info[key1][0]
            ssh2(ip, username, passwd, cmd)
            return m_mount_path


def config_cluster(s_mount_path,m_mount_path):
    # host_info = Helper.get_hostinfo()
    # username = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    mgmt_host_name = host_info['Management'][1]
    exit_flag = False
    for key1 in host_info.keys():
        if key1 == 'Management':
            ip = host_info[key1][0]
            #print 'Check the management instance.\n'
            # cmd = ['sudo service orcafs-mgmtd status','sudo service orcafs-mgmtd start']
            # if(cluster_ssh2(ip,username,passwd,cmd)):
            print 'Define the mamagement service running path.\n'
            cmd = ['sudo service orcafs-mgmtd status','sudo /opt/orcafs/sbin/orcafs-setup-mgmtd -p /'+m_mount_path+'/orcafs/beegfs_mgmtd','sudo systemctl start orcafs-mgmtd','sudo service orcafs-mgmtd status']
            #ssh2(ip, username, passwd, cmd)
            if (cluster_ssh2(ip, username, passwd, cmd)):
                print 'Mamagement service configured.'
                exit_flag=True
            else:
                sys.exit('Failed to configure mgmtd.')

        else:
            continue
    for key2 in host_info.keys():
        if key2 == 'Metadata':
            ip = host_info[key2][0]
            print 'Define a custom numeric metadata service ID (range 1..65535)\n'
            id = raw_input('Metadata Service ID:')
            cmd = ['sudo service orcafs-meta status','sudo /opt/orcafs/sbin/orcafs-setup-meta -p /'+m_mount_path+'/orcafs/orcafs_meta -s '+id+' -m '+mgmt_host_name,'sudo systemctl start orcafs-meta','sudo service orcafs-meta status']
            if (cluster_ssh2(ip, username, passwd, cmd)):
                print 'Metadata service configured.'
                exit_flag = True
            else:
                sys.exit('Failed to configure metadata.')
        elif key2 =='Storage':
            ip = host_info[key2][0]
            print 'Define a custom numeric storage service ID and numeric storage target ID (both in range 1..65535)\n'
            service_id =raw_input('Storage service ID:')
            target_id = raw_input('Storage target ID:')
            cmd = ['sudo service orcafs-storage status','sudo /opt/orcafs/sbin/orcafs-setup-storage -p /' + s_mount_path + '/orcafs_storage -s ' + service_id + ' -i '+target_id+' -m ' + mgmt_host_name,'sudo systemctl start orcafs-storage','sudo service orcafs-storage status']
            if (cluster_ssh2(ip, username, passwd, cmd)):
                print 'Storage service configured.'
                exit_flag = True
            else:
                sys.exit('Failed to configure storage.')
        else:
            continue

    for key3 in host_info.keys():
        if key3=='Client':
            ip = host_info[key3][0]
            print 'Define client mount directory with management service.\n'
            cmd = ['sudo service orcafs-client status','sudo /opt/orcafs/sbin/orcafs-setup-client -m '+mgmt_host_name,'sudo systemctl start orcafs-helperd','sudo systemctl start orcafs-client','sudo systemctl start orcafs-admon','sudo service orcafs-client status']
            ssh2(ip,username,passwd,cmd)
            if (cluster_ssh2(ip, username, passwd, cmd)):
                print 'Client service configured.'
                exit_flag = True
            else:
                sys.exit('Failed to configure client.')
        else:
            continue
    return exit_flag

def check_cluster_status():
    # host_info = Helper.get_hostinfo()
    # username = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    exit_flag = False
    for key in host_info.keys():
        if key =='Client':
            ip = host_info[key][0]
            print 'Check Cluster Connection.\n'
            cmd =['sudo orcafs-df']
            if (ssh2(ip, username, passwd, cmd)):
                exit_flag = True
    return exit_flag

if __name__=='__main__':
    print '\n'
    print '>>>>>>>>>>>>>>> This Script is used for OrcaFS Test Environment Setup <<<<<<<<<<<<<<<<<<\n\n'
    print '>>>>>>>>>>>>>>>Step1: Get the Servers Info<<<<<<<<<<<<<<<<<<\n'
    # server_Info = Helper.get_hostinfo()
    # print 'Server Role' + '\t\t' + 'Server IP Address' + '\t\t' + 'Server Hostname'
    # for key, value in server_Info.items():
    #     print key.ljust(10)+'\t\t'+value[0].ljust(17)+'\t\t'+value[1].ljust(10)
    #
    # print '\n>>>>>>>>>>>>>>>Step2: Install Required Basic Softwares on the Server<<<<<<<<<<<<<<<<<<\n'
    # username  = Helper.get_credential()['username']
    # passwd = Helper.get_credential()['password']
    # if install_basic():
    #     print 'All Basic SWs are installed on the servers\n'
    # else:
    #     print 'Install basic software failed'
    #     sys.exit(0)
    #
    # print '\n>>>>>>>>>>>>>>>Step3: Configure Host<<<<<<<<<<<<<<<<<<\n'
    # if write_etc_host():
    #     print 'Updated the host configuration\n'
    # else:
    #     print 'Config host failed'
    #     sys.exit(0)
    #
    # print '\n>>>>>>>>>>>>>>>Step4: Downloading and install the RPM packages.<<<<<<<<<<<<<<<<<<\n'
    # if rpm_Download():
    #     print 'All OrcaFS rpm are downloaded from ftp server.'
    # else:
    #     print 'Download RPM failed'
    #     sys.exit(0)
    #
    # print '\n>>>>>>>>>>>>>>>Step5: Install corresponding packages on the server.<<<<<<<<<<<<<<<<<<\n'
    # if remote_install():
    #     print 'All rpms are installed on the server'
    # else:
    #     print 'Install RPM failed'
    #     sys.exit(0)
    #
    print '\n>>>>>>>>>>>>>>>Step6: Create File System on the Storage Server.<<<<<<<<<<<<<<<<<<\n'
    s_mount_path = storage_mgmt()
    if s_mount_path:
        print 'Completed Storage Server RAID Configuration.'
    else:
        print 'Failed to configure RAID on the storage server'
        sys.exit(0)

    print '\n>>>>>>>>>>>>>>>Step7: Create File System on the Metadata Server.<<<<<<<<<<<<<<<<<<\n'
    m_mount_path=metadata_mgmt()
    if m_mount_path:
        print 'Completed Metadata Server RAID Configuration.\n'
    else:
        print 'Failed to configure RAID on the metadata server'
        sys.exit(0)

    print '\n>>>>>>>>>>>>>>>Step8: Configure the Cluster.<<<<<<<<<<<<<<<<<<\n'
    if config_cluster(s_mount_path,m_mount_path):
        print'Completed the cluster configuration.'
    else:
        print 'Failed to configure the cluster.'

    print '\n>>>>>>>>>>>>>>>Step9: Check the Cluster Status.<<<<<<<<<<<<<<<<<<\n'
    if check_cluster_status():
        print'Cluster Status is normal.'
    else:
        print 'Cluster Status is abnormal.'










