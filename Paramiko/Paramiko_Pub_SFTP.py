#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/ssh/id_rsa.txt')

transport = paramiko.Transport('192.168.29.79',22)
transport.connect(username='root',pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)

#upload
sftp.put(localpath,remotepath)

#download
sftp.get(remotepath,localpath)

transport.close()