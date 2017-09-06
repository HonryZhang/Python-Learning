#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'


#基于公钥密钥连接
'''
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('home/auto/.ssh/id_rsa')

#创建SSH对象

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.29.79',port=22,username='root',pkey=private_key)

stdin,stdout,stderr = ssh.exec_command('df')

res,err =stdout.read(),stderr.read()
result = res if res else err

print (result.decode())


#关闭连接
ssh.close()

'''
#SSH 封装Transport
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/id_rsa')
transport = paramiko.Transport(('192.168.29.79',22))

transport.connect(username='root',pkey=private_key)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin,stdout,stderr = ssh.exec_command('df')

res,err =stdout.read(),stderr.read()
result = res if res else err

print (result.decode())

transport.close()