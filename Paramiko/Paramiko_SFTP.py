#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import paramiko

transport = paramiko.Transport('192.168.29.79',22)
transport.connect(username='root',password='admin')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put(localpath,remotepath)

sftp.get(remotepath,localpath)

transport.close()