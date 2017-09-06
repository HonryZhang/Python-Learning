#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os

client = socket.socket()
# 声明socket类型，并生成socket连接对象
client.connect(('localhost', 8999))  # 连接服务器的IP地址和port

while True:
    msg = raw_input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    res_size = client.recv(1024) # 接受命令返回的长度
    print "命令长度大小：",res_size
    client.send("准备接收数据。")
    received_size = 0
    received_data=''
    while received_size < int(res_size.decode()):
        data = client.recv(1024)
        received_size+= len(data)
        received_data+=data
    else:
        print "receive done,total :",received_size
        print(received_data.decode('utf-8'))
# f = open('testsss.py', 'wb')
#    f.write(data)
#    f.close()

client.close()

# comment
