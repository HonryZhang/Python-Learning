#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import paramiko

#创建SSH 对象

ssh = paramiko.SSHClient()

#允许连接不在known_host文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.29.79',port=22,username='root',password='admin')

#执行命令
stdin,stdout,stderr = ssh.exec_command('df')

#获取命令结果
res,err =stdout.read(),stderr.read()
result = res if res else err

print (result.decode())


#关闭连接
ssh.close()
