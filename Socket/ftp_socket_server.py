#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import socket
import os
import hashlib
server = socket.socket() # 默认采用IPV4和TCP/IP协议
server.bind(('localhost',9999))
server.listen(5)

print "Now start to listen the call..."

while True:
    conn,addr = server.accept() # 将接收到的客户端实例化
    while True:
        print "Waiting for the call..."
        data = conn.recv(1024) # 开始接收客户端发送过来的数据
        print "received data:",data
        if len(data)==0: # 在Linux平台下，如果客户端中断后，服务端会一直接收空字符。如果接收到的数据为空，表示和客户端断开连接
            print "Lost the connection of Client..."
            break
        cmd,filename = data.split() # 服务端接收到的命令形式为：get xxxx
        if os.path.isfile(filename): # 判断文件是否存在
            f = open(filename,'rb') # 文件存在，读文件
            s_hash = hashlib.md5() # 生成一个md5 hash对象
            file_size = os.stat(filename).st_size # 获取文件的大小
            conn.send(str(file_size).encode()) # 将文件大小发送给客户端确认
            conn.recv(1024) # 获取客户端的确认信息
            for line in f.readlines(): # 循环读取文件每一行
                s_hash.update(line) # 对字符串进行md5更新处理，m.update(a)之后在 m.update(b)，相当于m.update(a+b)
                conn.send(line)
            print "the MD5 of the file:",s_hash.hexdigest() # 返回十六进制的加密结果
            f.close()
            conn.send(s_hash.hexdigest().encode()) # 将文件的加密结果发送给客户端
        print "File was sent to Client."
server.close()




