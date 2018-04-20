# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import os,paramiko,ConfigParser,sys,time,threading
from multiprocessing import Process,Pool
import base64
import readline

'''Return Command List'''
_BACK_CMD_LIST=('quit','q','exit','bye')

'''Do Nothing Command'''
_DO_NOTHING_CMD=('','\n','\r',None)

'''Prohibit or Disabled Commands'''
_FORBIDDEN_CMD = ('more','less','vi','top')

'''Process Pool Size'''
PROCESSES = 10

'''Basement Distributed File or Directory'''
DISTRUBUTE_BASE_DIR = '/tmp'

'''Initialize the conf file'''
class initConf:
    def __init__(self,conf_file):
        try:
            file_path = os.path.join((sys.path[0],conf_file))
            self.cf = ConfigParser.SafeConfigParser()
            self.cf.read(conf_file)
        except Exception as e:
            Log('RED','ConfigParserError:%s'%(str(e)))
            sys.exit(1)

#Read the configure file
#host_info = ['ip_address','username','password','port']
#servers_info = [host1,host2,host3]
    def readConf(self):
        servers_info = []
        try:
            opts = eval(self.cf.get('host','connList'))

            for opt in opts:
                host_info = []
                server_info = eval(self.cf.get('information',str(opt)))
                host_info.append(server_info['ip'])
                host_info.append(server_info['username'])
                host_info.append(base64.b64decode(server_info['password']))
                host_info.append(server_info['port'])
                servers_info.append(host_info)
        except Exception as e:
            Log('RED','ReadConfError:%s'%(str(e)))
            sys.exit(1)

        return  servers_info

'''Define the Log type and output format'''
def Log(type,msg):
    date_detail = time.strftime('%Y_%m_%d %H:%M:%S')
    logText = '[%s] %s'%(date_detail,msg)
    if type =='NORMAL':
        print '\033[32;1m%s\033[0m'%(msg)
    elif type == 'GREEN':
        print '\033[32;1m[INFO] %s\033[0m' % (logText)
    elif type == 'RED':
        print '\033[31;1m[ERROR] %s\033[0m' % (logText)
    elif type == 'YELLOW':
        print '\033[33;1m[WARN] %s\033[0m' % (logText)


'''Initialize the SSH service'''
def initSSH():
    paramiko.util.log_to_file("filename.log")
    server = paramiko.SSHClient()
    server.load_system_host_keys()
    server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return server

'''Define the user input entrance'''
def user_input(str):
    try:
        cmd = raw_input('\033[32;0m[%s]=>\033[0m' %(str)).strip()
        return cmd
    except KeyboardInterrupt:
        Log('NORMAL','\nKeyboardInterrupt')
        return None
    except Exception:
        print '\n'
        sys.exit(1)

'''Define shell command execution function'''
def ssh_run(host_info,cmd,ssh_server):
    try:
        ip,username,password,port = host_info[0],host_info[1],host_info[2],host_info[3]
        ssh_server.connect(ip,int(port),username=username,password=password,allow_agent=False,look_for_keys=False)
        stdin,stdout,stderr = ssh_server.exec_command(cmd,get_pty=True)
        cmd_result = stdout.read()
        #print cmd_result
        #print type(stderr.readlines())
        # if len(stderr.readlines()>0):
        #     Log('RED', '[%s]: %s' % (ip, stderr))
        if cmd_result!='':
            Log('NORMAL', '[%s]:%s' % (ip, cmd_result.rstrip()))
        # for res in cmd_result:
        #     print res
        #     if res=='':
        #         continue
        #     else:
        #         Log('NORMAL', '[%s]:%s' % (ip, res.rstrip()))
            # for line in res:
            #    # print line.rstrip()
            #     if line=='':
            #         continue
            #     else:
            #         Log('NORMAL','[%s]:%s'%(ip,line))
    except Exception as e:
        Log('RED', '[%s]: %s' %(ip,str(e)))

'''Define transfer file function'''
def distribute_file(host_info,filename):
    try:
        ip, username, password, port = host_info[0], host_info[1], host_info[2], host_info[3]
        RemoteFile = os.path.join(DISTRUBUTE_BASE_DIR,os.path.basename(filename))
        print RemoteFile
        trans = paramiko.Transport(ip,int(port))
        trans.connect(username = username,password = password)
        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.put(filename,RemoteFile)
        trans.close()
    except Exception as e:
        Log('RED', '[%s]: %s' % (ip, str(e)))
    else:
        Log('GREEN', 'Transfer %s to %s:%s Successfully!' % (filename, ip, RemoteFile))


'''Define command execution function based on action type'''
#def exeucte_cmd(servers_info,action,cmd,ssh_server):
def exeucte_cmd(servers_info,action,*args):
    start = time.time()
    #print cmd_args

    # p = Pool(processes=PROCESSES)
    # for host_info in servers_info:
    #     if action == 'ssh_run':
    #         p.apply_async(ssh_run,[host_info,]+cmd_args)
    #     elif action=='distribute_file':
    #         p.apply_async(distribute_file, [host_info,]+cmd_args)
    # p.close()
    # p.join()


    threads = []
    for host_info in servers_info:
        if action == 'ssh_run':
            t = threading.Thread(target=ssh_run, args=(host_info, args[0],args[1],))
            threads.append(t)
        elif action=='distribute_file':
            t = threading.Thread(target=distribute_file,args=(host_info,args[0],))
            threads.append(t)
    for t in threads:
        #t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    # for host_info in servers_info:
    #     if action == 'ssh_run':
    #         ssh_run(host_info,args[0],args[1])
    #     elif action=='distribute_file':
    #         distribute_file(host_info,args[0])
    end = time.time()
    print '\033[31;1mTotal Cost time:%ss\033[0m' % str(end - start)




def entryFunction(conf_name):
    p = initConf(conf_name)
    servers_info = p.readConf()
    ssh_server = initSSH()

    while True:
        print '''
    -------------------------
       [1]Execute command.
       [2]Transfer files.
       [q]Exit.
    -------------------------\n
    '''
        choice = user_input('Choice:')
        if choice=='1':
            while True:
                cmd = user_input('Current_CMD')
                if cmd in _BACK_CMD_LIST:
                    break
                elif cmd in _DO_NOTHING_CMD:
                    continue
                elif (set(_FORBIDDEN_CMD)&set(cmd.split()))!=set([]): #用户的输入的命令按空格拆分，并和禁用的命令求交集，如果不为空，说明存在禁用的命令
                    Log('RED','User can not use command which included in the forbidden commands:%s'%(str(_FORBIDDEN_CMD)))
                    continue
                exeucte_cmd(servers_info,'ssh_run',cmd,ssh_server)
        if choice=='2':
            while True:
                filename = user_input('Transfer')
                if filename in _BACK_CMD_LIST:
                    break
                elif filename==None:
                    continue
                file_check = os.path.isfile(filename)
                if file_check==False:
                    Log('YELLOW', 'The file does not exist or it is a directory!')
                    continue
                exeucte_cmd(servers_info,'distribute_file',filename)
        elif choice in _BACK_CMD_LIST:
            ssh_server.close()
            sys.exit()
        else:
            continue

if __name__=="__main__":
    # if len(sys.argv)<2:
    #     Log('RED', 'Usage: python %s example.conf' % (sys.argv[0]))
    #     sys.exit(1)
    # else:
    #     conf_name = sys.argv[1]
    #     entryFunction(conf_name)
    entryFunction('example.conf')






