#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import socket
import  hashlib
client = socket.socket() # 声明socket类型，并生成socket连接对象

client.connect(('localhost',9999)) # 连接server端

while True:
    cmd = raw_input(">>:").strip() # 输入客户端的指令
    if len(cmd)==0: # 判断输入是否为空
        continue
    if cmd.startswith('get'): # 如果命令是以get 开头
        client.send(cmd)
        response_size = client.recv(1024) # 客户端接收到服务端发送回来的文件大小
        print "the total size of the file:",int(response_size.decode())
        client.send('Client is ready for receiving file...') # 客户端确认文件大小，并做好接收准备
        received_size = 0
        file_name = cmd.split()[1] # 获取要传送的文件名
        f = open(file_name+'.new','wb') # 打开文件，并准备写入
        c_hash = hashlib.md5() # 生成一个md5 hash对象
        while received_size < int(response_size): # 如果接收到的数据大小小于文件的总大小
            if int(response_size)-received_size > 1024: # 如果剩下的数据大小大于1024,则每次接收1024B并循环接收
                remaining_size = 1024
            else:
                remaining_size = int(response_size)-received_size # 直到最后剩下的数据量少于1024B
            data = client.recv(remaining_size) # 客户端接收文件
            received_size += len(data) # 接收到问文件总大小
            c_hash.update(data) # 对字符串进行md5更新处理
            f.write(data) #将接收到的数据写入新文件
        else:
            received_file_md5 = c_hash.hexdigest() # 接收到的文件的加密结果
            print "File was received. Source File Size and Received File Size:",response_size,received_size
            f.close()
    file_md5 = client.recv(1024) # 接收服务端发送过来的源文件加密结果
    print "The Source file MD5 is:",file_md5
    print "The Received file MD5 is:",received_file_md5
client.close()






