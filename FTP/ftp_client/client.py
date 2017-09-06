#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import socket
import os,sys
import getpass

class Client(object):
    def __init__(self,host,port):
        self.sock = socket.socket()
        self.sock.connect((host,port))
        self.exit_flag = False
        if self.auth():
            self.interactive()
    fun_dict = {
        'help':'help',
        'get':'get_file',
        'put':'put_file',
        'ls':'list_file',
        'cd':'change_dir',
        'del':'delete'
    }

#fuction to verify the authentication of the login user
#user input: <username>
#auto prompt 'Password:',user input the password
#the whole auth string is: <ftp_auth>|<username>|<password>
    def auth(self):
        retry_count = 0
        while retry_count<3:
            username = raw_input("Input the username:").strip()
            if len(username)==0:continue
            passwd =getpass.getpass()
            auth_str = "ftp_auth|%s|%s"%(username,passwd)

            self.sock.send(auth_str)

            auth_response = self.sock.recv(1024)
            if auth_response =='ftp_auth::success':
                print "User Authentication Passed."
                self.username = username
                self.cur_path = username
                return True
            else:
                print 'Wrong username or password, you have 3 times to retry..'
                retry_count +=1
        else:
            print "Too many attempts, exit"

    def interactive(self):
        try:
            while not self.exit_flag:
                cmd = raw_input('%s:%s>>:'%(self.username,self.cur_path)).strip()
                if len(cmd)==0: continue
                cmd_parse = cmd.split()
                msg_type = cmd_parse[0]
                if self.fun_dict.has_key(msg_type):
                    func = getattr(self,self.fun_dict[msg_type])
                    func(cmd_parse)
                else:
                    print "Invalid command type, type[help] to see supported command"
        except KeyboardInterrupt:
            self.exit('exit')
        except EOFError:
            self.exit('exit')

#functin to list the files in the current directory
#the cmd type : list_file ls xxxx
#the msg type1: ls
#the msg type2: ls dir_path, such as ls /home/, ls /etc/ssh/
    def list_file(self,msg):
        #the cmd is 'list_file| ' or 'list_file|/etc/ssh/'
        cmd = 'list_file|%s'%(' '.join(msg[1:]))
        self.sock.send(cmd)

        server_confirm_msg = self.sock.recv(1024)
        if server_confirm_msg.startswith('message_transfer::ready'):
            server_confirm_msg = server_confirm_msg.split('::')
            msg_size = int(server_confirm_msg[-1])
            self.sock.send('message_transfer::ready::client')
            recv_size = 0
            while not msg_size == recv_size:
                if msg_size-recv_size>1024:
                    data = self.sock.recv(1024)
                else:
                    data = self.sock.recv(int(msg_size-recv_size))
                recv_size += len(data)
                sys.stdout.write(data)

# function to switch to the specified directory
# the cmd type : change_dir dir_path
# the msg type1: cd
# the msg type2: cd dir_path, such as cd /home/, cd /etc/ssh/

    def change_dir(self,msg):
        #the cmd is 'change_dir|cd ' or 'change_dir|cd /home/'
        cmd = 'change_dir|%s' % (' '.join(msg))
        self.sock.send(cmd)

        server_res = self.sock.recv(1024)
        if server_res.startswith('change_dir::ok'):
            self.cur_path = server_res.split('::')[-1]
        else:
            print 'the path is %s'%server_res.split('::')[-1]

# function to delete to the specified directory or file
# the cmd type : delete_file dir_path or single file
# the msg type: rm xxx/xxxx
    def delete(self,msg):
        if len(msg)>1:
            cmd = 'delete_file|%s'%' '.join(msg[1:])
            self.sock.send(cmd)
        else:
            print "Wrong command"

#function to put file to the destination folder
# the cmd type : put_file put xxx
# the msg type: put local_file
    def put_file(self,msg):
        if len(msg) == 2:
            if os.path.isfile(msg[1]):
                file_size = os.path.getsize(msg[1])
                cmd = 'file_transfer|put|send_ready|%s|%s'%(msg[1],file_size)
                self.sock.send(cmd)

                server_res = self.sock.recv(1024)
                print "===>",server_res

                progress_percent = 0
                if server_res.startswith("file_transfer::put_file::recv_ready"):
                    f = open(msg[1],'rb')
                    sent_size = 0
                    while not sent_size == file_size:
                        if file_size-sent_size <= 1024:
                            data = f.read(file_size-sent_size)
                            sent_size += file_size-sent_size
                        else:
                            data = f.read(1024)
                            sent_size+=1024
                        self.sock.send(data)

                        cur_percent = int(float(sent_size)/file_size*100)
                        if cur_percent > progress_percent:
                            progress_percent = cur_percent
                            self.show_progress(file_size,sent_size,progress_percent)
                    else:
                        print "send file :%s, done"%msg[1]
                    f.close()

# function to get file from the remote
# the cmd type : get_file get xxx
# the msg type: get remote_file
    def get_file(self,msg):
        if len(msg)==2:
            cmd = "file_transfer|get|%s"%msg[1]
            self.sock.send(cmd)

        server_response = self.sock.recv(1024)
        if server_response.startswith("file_transfer::get_file::send_ready"):
            file_size = int(server_response.split('::')[-1])
            print 'file size:------>',file_size
            file_name = os.path.basename(cmd.split('|')[-1])
            print 'file name:------>',file_name
            f = open(file_name,'wb')
            self.sock.send('file_transfer::get_file::recv_ready')

            recv_size = 0
            progress_percent = 0
            while not recv_size ==file_size:
                data = self.sock.recv(file_size-recv_size)
                recv_size+= len(data)
                f.write(data)

                cur_percent = int(float(recv_size)/file_size*100)
                if cur_percent > progress_percent:
                    progress_percent = cur_percent
                    self.show_progress(file_size,recv_size,progress_percent)
            else:
                print "received the file done"
            f.close()
        else:
            print "the result:%s"%server_response


    def show_progress(self, total, finished, percent):

        progress_mark = "=" * (percent / 2)
        sys.stdout.write("[%s/%s]%s>%s\r" % (total, finished, progress_mark, percent))
        sys.stdout.flush()
        if percent == 100:
            print '\n'

    def help(self, msg):
        print'''
            command_type    command_instruction
            help            help
            get             get remote_filename
            put             put local_filename
            exit            exit the system
            ls              list all the files int the current directory
            del             del the remote filename
            cd              cd  the dest_dir
        '''

    def exit(self,msg):
        self.sock.shutdown(socket.SHUT_WR)
        sys.exit("Bye! %s" % self.username)


if __name__=="__main__":
    s = Client('localhost',9999)

