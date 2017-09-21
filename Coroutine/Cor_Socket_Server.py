#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import sys,socket,time,gevent

from gevent import socket,monkey

monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        gevent.spawn(handle_request,conn)

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print "recv data:",data
            conn.send(data+'ok')
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print ex

    finally:
        conn.close()

if __name__ =="__main__":
    server(8002)