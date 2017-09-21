#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import socket

Host = 'localhost'
port = 8002

s = socket.socket()
s.connect((Host,port))
while True:
    msg = raw_input('>>:')
    s.sendall(msg)

    data = s.recv(1024)
    print 'Client Recved:',repr(data)
s.close()