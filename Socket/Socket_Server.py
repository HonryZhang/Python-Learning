#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket
import os,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

server = socket.socket()  # 实例化一个socket

server.bind(('localhost', 8999))  # 绑定监听端口
server.listen(5)  # 监听，最多允许5个连接

print "Listing the call...."
while True:
    conn, addr = server.accept()  # 等待电话进来,conn就是客户端连接过来而在服务端为其生成的一个连接实例
#    print conn, addr

    while True:
        print 'Call is comming...'
        data = conn.recv(1024)
        print "recv:", data
        if not data:
            print"client has lost...."
            break
        print "Now executing command:",data
        res = os.popen(data.decode('utf-8')).read()  # 接受字符串，返回结果也是字符串
        print "Before send:", len(res)
        if len(res) == 0:
            res = "client has no output好多撒"
        #        conn.send(data.upper())
        conn.send(str(len(res.encode())).encode('utf-8')) # 先发送大小给客户端
        client_ack = conn.recv(1024)# 等待客户端确认消息
        print "确认消息：",client_ack
        conn.send(res.encode('utf-8'))
        print 'send done'
# f = open('Socket_Server.py')
#        data = f.read()
#        conn.send(data)

server.close()
