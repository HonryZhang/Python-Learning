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

'''
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


# def help(self):
#     print '''
#     command_type    command_instruction
#     help            help
#     get             get remote_filename
#     put             put local_filename
#     exit            exit the system
#     ls              list all the files int the current directory
#     del             del the remote filename
#     cd              cd  the dest_dir
#     '''
#
# print os.path.dirname(__file__)
    


#九九乘法表
'''
def gen(line_cnt):
    for i in range(1,line_cnt+1):
        for j in range(1,i+1):
            m= i*j
            print '%s * %s = %s\t'%(i,j,m)
if __name__ =="__main__":
    gen(9)
'''

#互不相同无重复的数字
# cnt = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 print i*100+j*10+k
#                 cnt +=1
# print cnt

#!/usr/bin/python
#-*- coding:utf-8 -*-

#from math import sqrt
# def number():
#     for i in range(100,201):
#         flag = 1
#         k = int(sqrt(i))
#         for j in range(2,k+1):
#             if i%j ==0:
#                 flag =0
#                 break
#
#         if flag==1:
#             print '%5d\n'%i,
#     b1 = [1, 2, 3]
#     b2 = [2, 3, 4]
#     b3 = [val for val in b1 if val  in b2]
#     print b3
# if __name__ =="__main__":
#     number()

# List = ['1','2','4','2']
# d=[6,5,7,8,9,0]
# b = {}
# b = b.fromkeys(a)
# print b.values()
# c = list(b.keys())
# print c

# a = [1,2,3,4,5,6]
# d=[6,5,7,8,9,0]
# a.append(23)
# a.extend(d)
# print a

# print a+d
# import random
# import string
# a = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
# print a
#
# aList = ['1','2','4','2']
# aList.append( 2009 )
# print "Updated List : ", aList
#
# for i in range(1,10):
#     print '\n'
#     for j in range(1,10):
#         if(i>=j):
#             print '%d*%d=%d' % (i, j, i * j),

#!/usr/bin/python
#-*- coding:utf-8 -*-

# mylist = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9]

# myset = set(mylist)

# print myset

# for item in myset:
#     print item, mylist.count(item)

# for i in range(1,10):
#     print '\n'
#     for j in range(1,10):
#         if(i>=j):
#             print '%d*%d=%d' % (i, j, i * j),
# num = 22
# matrix=[[1,3,15,17,19],
#             [2,4,16,18,22],
#             [3,6,21,22,51],
#             [6,8,22,29,57]]
# last_col_list=[one_list[-1] for one_list in matrix]
# index_list = []
# for i in range(len(last_col_list)):
#     if last_col_list[i] >= num:
#         index_list.append(i)
# print last_col_list
# print index_list
# res_list=[]
# while index_list:
#     one_row=index_list.pop()
# #    print one_row
#     one_list=matrix[one_row]
# #    print  one_list
#     if num in one_list:
#         tmp_str = one_list.index(num)
#         res_list.append(tmp_str)
#         print res_list
#         print 'num exist in the matrix:',num
#
# print 34%10,3%10
'''
def digitCounts(k, n):
    i=j=num=0
    if k==0:
         num=1
    for i in range(n):
        j=i
        while j!=0:
            if j%10==k:
                num+=1
            j=j/10

    print num
digitCounts(2,127)

# '''
# import fileinput,socket
#
# def main():
#     options = gather_information(get_defaults())
#     print options
#     hostname = socket.gethostname()
#     print 'the current hostname:',hostname
#
# def get_defaults():
#     return {
#         'management_node': 'name',
#         'management_ip':'1.1.1.1',
#
#     }
# def gather_information(defaults):
#     options = {}
#     options['management_node'] = default_prompt('Management Node', defaults['management_node'])
#     return options
#
# def default_prompt(name, fallback):
#     response = raw_input(name + '(' + fallback + ')'":")
#     #assert isinstance(response, str)
#     if (response):
#         return response
#     else:
#         return fallback
#
# main()

# lista = [1,2,3,4]
# cmd='mdadm --create /dev/md1 --level=1 --raid-devices='+str(len(lista))
# a = int(len(lista))
# for disk in lista:
#     cmd+= ' '+str(disk)
#
#
# print cmd

# import re
# str = '''Personalities : [raid0] [raid1]
# md2 : active raid1 sde[1] sdd[0]
#       8380416 blocks super 1.2 [2/2] [UU]
#
# md1 : active raid0 sdc[1] sdb[0]
#       16760832 blocks super 1.2 512k chunks'''
#
# while True:
#     s_raid_type = raw_input('Select the Storage Server RAID Type <5 or 6>:').rstrip()
#     print s_raid_type
#     if s_raid_type.isdigit():
#         print 'data'
#     if (s_raid_type) !='ext4' and (s_raid_type) !='xfs':
#         print 'No matched RAID Type, select again.\n'
#
#     else:
#
#         break

'''
import paramiko,sys,os
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
           # print "err_list:",err_list
            print "out_listxxxxxxxxxxxx:", stdout.readlines()
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
                    else:
                        print out
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

 #       sys.exit('Connection Failed')
if __name__ =="__main__":
    ip ='192.168.10.249'
    username ='root'
    passwd = 'admin'
    #cmd=['/opt/orcafs/sbin/orcafs-setup-mgtd -p /data/orcafs/orcafs_mgmtd','dsad']
    #cmd = ['sudo curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo']
    cmd =['cd fio && ./configure && make && make install']
    #cluster_ssh2(ip, username, passwd, cmd)
    if(cluster_ssh2(ip,username,passwd,cmd)):
        print 'xxx',
    else:
        print 'uuu',
    # print('This is a \033[1;31m test \033[0m!')

'''

# import sys
#
# def exitfunc(value):
#     print value
#     sys.exit(0)d
#
# print "hello"
#
# try:
#     sys.exit(1)
# except SystemExit,value:
#     exitfunc(value)
#
# print "come?"
'''
import time,threading,sys


def run():
    try:
        for i in range(1,5):
            print 'Current name:', threading.current_thread().name
            if i>3:
                sys.exit('\033[1;31m Error: Incorrect Command:\033[0m')
        return True
    except SystemExit, value:
        print '%s' % ( value)
        return False


def thread():
    start_time = time.time()

    print 'Main:', threading.current_thread().name
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()

    print 'Main over' , threading.current_thread().name
    print 'Total:', time.time()-start_time
    return True

if __name__ == '__main__':
    thread()
'''
'''
import paramiko,sys
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            print 'Current CMD is:',m
            stdin,stdout,stderr = ssh.exec_command(m,get_pty=True)
            print 'out:',stdout.readlines()
            print 'err:',stderr.readlines()
            out = stdout.readlines()
            for o in out:
                print o.rstrip()
        print '%s:\tOK\n'%(ip)
        ssh.close()
        return True
    except:
        print '%s:\tError\n'%(ip)
        sys.exit('Connection Failed')

if __name__=='__main__':
    ip ='192.168.10.249'
    username ='root'
    passwd = 'admin'
    cmd = ['cd fio && ./configure && make && make install']
    ssh2(ip, username, passwd, cmd)

'''

'''
def remote_install():
    #local_remote_file=dict()
    username  = 'root'
    passwd = '11'

    local_remote_file={'Remote_install_rpm.py':'/root/Remote_install_rpm.py','hostconfig':'/root/hostconfig','Helper.py':'/root/Helper.py'}
    for v in range(1,3):
        print 'ip address:', v
        ip = v
        get_value(ip,username,passwd,**local_remote_file)
    #cmd = ['python Remote_install_rpm.py','rm -rf Remote_install_rpm.py','rm -rf hostconfig','rm -rf Helper.py']
    #thread_run(cmd)
    #return True
def get_value(ip,username,passwd,**kwargs):
    print 'Ip:',ip
    print 'name:',username
    print 'passwd:',passwd
    for k,v in kwargs.items():
        print 'k:',k + ' | '+'v:',v

remote_install()
'''

# str = 'loveleetcode'
# print str[::-1]
# print str[:-5:-3]
# for i in range(len(str)):
#     str1 = str[i+1:]
#     if (str[i] not in str1) and (str[i] not in str[0:i]):
#         print str[i],i

# def outer():
#     x = 10
#     def inner():
#         print x
#
#     return inner
#
# outer()()
#
# f = outer()
# f()
#list = [1,2,4,5,6,7,7]
#print map(lambda x:list[x-1],map(lambda x:x%2==0,range(1,len(list))))
#print filter(lambda x:x%2==0,range(len(list)))
#print reduce(lambda x,y:x+y,map(lambda x:x+3,map(lambda x:list[x-1],map(lambda x:x%2==0,range(1,len(list))))))
#print reduce(lambda x,y:x+y,map(lambda x:x+3,map(lambda x:list[x],filter(lambda x:x%2==0,range(1,len(list))))))
import collections
# s = 'asdr'
# wanted = collections.Counter(s)
# print wanted
# for i,c in enumerate(s):
#     print i,c

#
# list = [1,2,3,4,5,6]
# print [list[i] for i in list if i%2==0]
# print map(lambda x:x+3,map(lambda x:list[x-1],filter(lambda x:x%2==0,range(1,len(list)+1))))
# def remove(alist):
#     for i in alist:
#         if i % 2 == 0:
#             del alist[alist.index(i)]
#     print sum(alist)
#
# remove(list)

#
'''
def getminWindow(source, target):
    score = 0
    wanted = collections.Counter(target)#get the char count in the target string
    start, end = 0, len(source)
    tmp = {} #define a temp dictionary, the key is the char, the value is the count
    tmp_list = collections.deque([]) #get the matched char index
    for index, char in enumerate(source):
        if char in wanted:
            tmp_list.append(index)   #获取字符的索引
            tmp[char] = tmp.get(char, 0) + 1 #如果字符不存在新的字典中，则加入并且 value+1,如果已经存在，value 直接+1，#if the value of tmp[char] not exist, add into the dict
           # print tmp.get(c,0)
            #print d
            print 'tmp_dict',tmp
            print 'tmp_list',tmp_list
            if tmp[char] <= wanted[char]:
                print int(tmp[char])  #
                print int(wanted[char])
                score += 1  #score的值匹配 target的长度
            print tmp_list[0]
            print source[tmp_list[0]]
            print tmp[source[tmp_list[0]]]
            print wanted[source[tmp_list[0]]]
            while tmp_list and tmp[source[tmp_list[0]]] > wanted[source[tmp_list[0]]]:

                tmp[source[tmp_list.popleft()]] -= 1
                print tmp
                print tmp_list
            if score == len(target) and tmp_list[-1] - tmp_list[0] < end - start:
                start, end = tmp_list[0], tmp_list[-1] #return the matched index
    print  source[start:end + 1]
    print tmp_list
#
source = "ADBEBANC"
target="ABC"
getminWindow( source, target)
'''

# def getMinWindow(source,tar):
#     count = 0
#     start=0
#     end=0
#     tar_dict = collections.Counter(tar) #get the char count in the target string
#     tmp_dict = {}   #define a temp dictionary, the key is the char, the value is the count
#     tmp_list = []   #define a temp list
#     for k,v in enumerate(source):  #get the char and the index info of source string
#         if v in tar_dict:  #if the char in the target str(tmp_dict)
#             tmp_list.append(k) # add the index to a temp list
#             tmp_dict[v] = tmp_dict.get(v, 0) + 1 # if the key is v, get the value. if not exist, add 1 time
#             if tmp_dict[v]<=tar_dict[v]:
#                 count +=1
#             if tmp_list and tmp_dict[source[tmp_list[0]]]> tar_dict[source[tmp_list[0]]]:
#                 tmp_dict[source[tmp_list.pop(0)]]-=1
#             if count ==int(len(tar)):
#                 start,end = tmp_list[0],tmp_list[-1]
#     print source[start,end+1]
#
# s = "ADOBECODEBANC"
# t="ABC"
# getMinWindow( s, t)


# def reverse(str):
#     result = str.split(' ')
#     print result
#     for i in range(len(result)/2):
#         result[i],result[len(result)-1-i] = result[len(result)-1-i],result[i]
#     str = ' '.join(result)
#
#     print str
#
# reverse('this is a test script')
# reverse('hello smart guy')
# a =[3,4,6,5,3]
# print reduce(lambda x, y: x+y, [a[x]+(x)%2*3 for x in range(len(a))])


'''
import sys,re
#sys.path.append('../Paramiko')
def get_hostinfo():
    host_info = {}
    with open('/Users/hongrui/PycharmProjects/Orcadt/Python-Learning/Paramiko/hostconfig') as f:
        for line in f.readlines():
            line_list = re.split(r'\s+', line.rstrip())
            info = [line_list[1], line_list[2]]
            host_info[line_list[0]] = info
    f.close()
    #key= list(host_info)[0]
    #print key
    return host_info
#get_hostinfo()

#m_raid_name = 'md0'
#m_raid_type = '5'
#m_mount_path = 'mnt/md0'

host_info = get_hostinfo()
metadata_server_info ={}
storage_server_info ={}
for k,v in host_info.items():
    #print 'v:',v
    if v[1]=='Metadata':
        m_raid_name = raw_input('raid_name:')
        m_raid_type = raw_input('raid_type:')
        m_mount_path = raw_input('path:')

        metadata_server_info[k] = [
                            {
                                'raid_name': m_raid_name,
                                'raid_type': m_raid_type,
                                'mount_path': m_mount_path,
                                'host_role': v[1] ,
                                'ip':v[0]
                            }
                        ]
    elif v[1]=='Storage':
        s_raid_name = raw_input('raid_name:') 
        s_raid_type = raw_input('raid_type:')
        s_mount_path = raw_input('path:')
        storage_server_info[k] = [
                            {   'raid_name': s_raid_name,
                                'raid_type': s_raid_type,
                                'mount_path': s_mount_path,
                                'host_role': v[1] ,
                                'ip':v[0]
                            }
                        ]
info = dict(storage_server_info,**metadata_server_info)
print info

for key,values in info.items():
    for value in values:
        print value
        if value['host_role']=='Storage':
            path = value['mount_path']
            print path ,key ,value['ip']

'''


# params = {"username":['testname',123], "passwd":['class',234],'abx':['age',344],"usee":['tame',123]}
# pa =    {"user":['testname',123], "ttt":['class',234]}
#
# d={'a':1,'b':2,'c':3}
#
# dd={'c':11,'d':22,'e':33}
# d.update(dd)
# print d
# params.update(pa)
# print params
# p = dict(pa,**params)
# print p

'''
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
    #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i*2

#使用for循环
for i in yield_test(5):
    print(i,",")


def ch1(num):
    s = []
    for i in range(4):
        s.append(str(num % 256))
        num /= 256


    print '.'.join(s[::-1])
ch1(123456778)
import commands,os
s_mount_path = raw_input('Input the filesystem mount path of Storage Server %s:')
os.system('sudo mkdir -p '+s_mount_path)
os.system('touch xxx')
print os.getcwd()
print s_mount_path
'''
import re
str = '''<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">1，node1，node2，node3一共3个主机节点，这3个节点都为osd，mon节点，每个节点上若干个osd进程，其中node1是leader mon
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">2，集群状态正常，已经创建了rbd pool和rbd image，已经将rbd image在client端通过NBD的方式导出
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">3，副本数为2
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">4，客户端、服务器前端与Public Switch连接正常，服务器后端与Cluster Switch连接正常
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">5，在client端将nbd0（pool1）和nbd1（pool2）都创建成ext4的文件系统，分别挂载到/nbd0 和/nbd1目录下，在/nbd0 目录下写一个20G大小的文件20g.file，完成后拷贝到/nbd1目录下
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">6，拷贝完成后，对nbd0和nbd1做快照
<div style="margin: 0px; padding: 0px; font-family: &quot;Trebuchet MS&quot;, Arial, Verdana, sans-serif; font-size: 12px; background-color: rgb(238, 238, 238);">7，对两个文件系统/nbd0 /nbd1进行写文件操作（一个写同名文件，rate=200k，保证COW持续的时间长，一个写不同名称的文件），对裸设备nbd2（pool1），nbd3（pool2）进行裸设备随机读写'''

print type (str)
pattern = '<div style="(.+)">$'
#res = str.replace('<p>','').replace('^<img','q')
#print res
res1 = re.sub('<div.+">','',str)
print res1

#url = 'https://113.215.20.136:9011/113.215.6.77/c3pr90ntcya0/youku/6981496DC9913B8321BFE4A4E73/0300010E0C51F10D86F80703BAF2B1ADC67C80-E0F6-4FF8-B570-7DC5603F9F40.flv'
#pattern = 'https://(.*?):9011/'
#out = re.sub(pattern, 'https://127.0.0.1:9091/', url)
#print out