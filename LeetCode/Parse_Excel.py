# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

'''
Requirement:
1> Check the login password
2> Check the health of the host
3> Distribute files to different host
'''

'''
The content of Excel file:
The sheet name should be 'Information'
The server info is start from Row2:
hostname    IP_address  port    username    password
'''

'''
The content of conf file:
[host]
connList=['host1','host2','host3']

[information]
host1=('ip':'192.168.100.244','port':'22','username':'root','password':'encryption string'}
host2=('ip':'192.168.100.245','port':'22','username':'root','password':'encryption string'}
host3=('ip':'192.168.100.246','port':'22','username':'root','password':'encryption string'}

'''
import os,sys,xlrd,base64

#Parse file content based on the file extension

def parserFile(fileName):
    _list = []
    _hosts = []
#    print fileName.split('.')
    if fileName.split('.')[1]=='xlsx':
        print 'Start to parse the excel file...'
        data = xlrd.open_workbook(fileName)
        table = data.sheet_by_name('Information')
        nrows = table.nrows
        for i in range(nrows-1):
            hostname = table.cell(i+1,0).value
            ip = table.cell(i+1,1).value
            port = int(table.cell(i+1,2).value)
            username = table.cell(i+1,3).value
            password = base64.b64encode(str((table.cell(i+1,4)).value))
            _hosts.append(hostname)
            _list.append('''%s={'ip':'%s','port':'%s','username':'%s','password':'%s'}'''%(hostname,ip,port,username,password))
    elif fileName.split('.')[1]=='txt':
        print 'Start to parse the txt file...'
        with open (fileName,'r') as f:
            for line in f:
                _info = line.split()
                hostname = _info[0]
                ip = _info[1]
                port = _info[2]
                username = _info[3]
                password = base64.b64encode(str(_info[4]))
                _hosts.append(hostname)
                _list.append('''%s={'ip':'%s','port':'%s','username':'%s','password':'%s'}'''%(hostname,ip,port,username,password))
    else:
        raise Exception('Only support .txt and .xlsx file...')
    print 'Parse Completed.'
    return _list,_hosts

#Write the parsed contents to conf file

def writeToConf(str):
    with open('example.conf','ab+')as f:
        f.write('%s\n'%str)

#If example.conf already existed, delete first

def checkFiles():
    print 'Checking the example file...'
    if os.path.exists('example.conf'):
        print 'example file exists, now deleting'
        os.remove('example.conf')
    else:
        print 'Could not find the example.conf, now generating'

if __name__=='__main__':
    checkFiles()
    if len(sys.argv)<2:
        print '''Usage: python %s example.xlsx'''%(sys.argv[0])
        sys.exit()
    else:
        if not os.path.exists(sys.argv[1]):
            raise Exception('The file not exist.')
        _list,_hosts = parserFile(sys.argv[1])
        print 'Now start to write host info to conf file...'
        writeToConf('[host]')
        writeToConf('connList=%s'%(str(_hosts).replace('u\'','\'')))
        writeToConf('\n[information]')
        for _ in _list:
            writeToConf(str(_))
        print 'Completed to write host info to example.conf file. exiting...'