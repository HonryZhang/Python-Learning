#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import SocketServer
import os,sys,commands
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from  conf import  account


class MyTCPHandler(SocketServer.BaseRequestHandler):
    exit_flag = False

#All the interactive operations with clients are handled in the function<handle>
#the whole auth string is: <operation>|<para1>|<para2>...
#the msg is a list: ['<operation_type>','<para1>','<para2>'...]
#the parameters type: filename/dir_path/file_path...

    def handle(self):
        while not self.exit_flag:
            msg = self.request.recv(1024)
            if not msg:
                break
            msg_parse = msg.split('|')
            msg_type = msg_parse[0]
            if hasattr(self,msg_type):
                func = getattr(self,msg_type)
                func(msg_parse)
            else:
                print 'Wrong message type %s'%msg_type

#function to get the anthentication of the user
#the whole auth string is: <ftp_auth>|<username>|<password>
#the msg is ['ftp_auth','<username>','<password>']
    def ftp_auth(self,msg):
        auth_res = False
        if len(msg) ==3:
            msg_type,username,passwd = msg

            if account.accounts.has_key(username):
                if account.accounts[username]['passwd'] == passwd:
                    auth_res = True
                    self.login_user = username
                    print os.path.dirname(__file__)
                    self.cur_path = '%s/%s'%(os.path.dirname(__file__),account.accounts[username]['home'])
                    self.home_path = '%s/%s'%(os.path.dirname(__file__),account.accounts[username]['home'])
                    print self.cur_path
                else:
                    auth_res = False
            else:
                auth_res = False
        else:
            auth_res = False
        if auth_res:
            msg = '%s::success'%msg_type
            print 'User %s has passed the authentication'%username
        else:
            msg = '%s::failed' % msg_type
        self.request.send(msg)

#function to list the files in the current directory
#the msg is ['list_file','<path>']
    def list_file(self,msg):
        # the cmd is 'cd <cur_path>; ls -lh  or ls -lh /etc/ssh'
        print self.cur_path
        cmd = 'cd %s; ls -lh %s' %(self.cur_path,' '.join(msg[1:]))
        files = os.popen(cmd).read()
        confirm_msg = 'message_transfer::ready::%s'%str(len(files))
        self.request.send(confirm_msg)

        confirm_from_client = self.request.recv(1024)
        if confirm_from_client == "message_transfer::ready::client":
            self.request.sendall(files)

# function to switch to the specified directory
# the msg is ['change_dir','cd' or 'cd /home/']

    def change_dir(self,msg):
        change_res = ''
        msg = msg[-1].split()
        # no dir follows cd command, switch to the home directory
        if len(msg)==1:
            print self.home_path
            print self.cur_path
            self.cur_path = self.home_path
            print self.cur_path
            relative_path = self.cur_path.split(self.home_path)[-1]
            change_res = 'change_dir::ok::%s'%relative_path
        if len(msg)==2:
            if os.path.isdir("%s/%s")%(self.cur_path,msg[-1]):
                abs_path = os.path.abspath("%s/%s%"%(self.cur_path,msg[-1]))
                if abs_path.startswith(self.home_path):
                    self.cur_path = abs_path
                    relative_path = self.cur_path.split(self.home_path)[-1]
                    change_res = 'change_dir::ok::%s'%relative_path
                else:
                    change_res = "change_dir::error::target dir doesn't exist"
            else:
                change_res = "change_dir::error::target dir doesn't exist"
        else:
            change_res = "change_dir::error::Error:wrong command usage."
        self.request.send(change_res)

# function to delete to the specified directory or single file
# the msg is ['delete_file','dir' or 'file']
    def delete_file(self,msg):
        file_list = msg[1].split()
        res_list = []
        for i in file_list:
            abs_file_path = "%s/%s"%(self.cur_path,i)
            cmd_res = commands.getstatusoutput("rm -rf %s"%abs_file_path)[1]

#function to verify the file path
    def has_privilege(self, path):
        abs_path = os.path.abspath(path)
        if abs_path.startswith(self.home_path):
            return True
        else:
            return False
#function to get or put the files
#the msg type is ['file_transfer', 'get or put','file']
    def file_transfer(self,msg):
        trans_type = msg[1]
        file_name = '%s/%s'%(self.cur_path,msg[2])
        self.has_privilege(file_name)
        if trans_type == 'get':
            if (os.path.isfile(file_name)) and self.has_privilege(file_name):
                file_size = os.path.getsize(file_name)
                confirm_msg = "file_transfer::get_file::send_ready::%s"%file_size
                self.request.send(confirm_msg)

                client_confirm_msg = self.request.recv(1024)
                if client_confirm_msg == "file_transfer::get_file::recv_ready":
                    f = open(file_name,'rb')
                    size_remaining = file_size
                    while size_remaining >0:
                        if size_remaining <1024:
                            self.request.send(f.read(size_remaining))
                            size_remaining = 0
                        else:
                            self.request.send(f.read(1024))
                            size_remaining -=1024
                    else:
                        print "Send file done..."
            else:
                err_msg = "file_transfer::get_file::error::file does not exist or is a directory"
                self.request.send(err_msg)

        elif trans_type == 'put':
            file_name,file_size = msg[-2],int(msg[-1])
            file_name = '%s/%s'%(self.cur_path,file_name)
            print "the file name is: %s"%file_name

            if os.path.isfile(file_name):
                f = open('%s.0'%(file_name),'wb')
            else:
                f = open('%s'%(file_name),'wb')
            confirm_msg = "file_transfer::put_file::recv_ready"
            self.request.send(confirm_msg)

            recv_size = 0
            while not recv_size == file_size:
                data = self.request.recv(1024)
                recv_size += len(data)
                f.write(data)
            else:
                print "Receive file:%s done" % (file_name)
                # print len(file_content), file_content[-100:]
                f.close()

if __name__ == "__main__":
    HOST, PORT = 'localhost', 9999

    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
