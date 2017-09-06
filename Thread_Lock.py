#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import threading
import time
num = 0
lock = threading.Lock()
def run(n):
    lock.acquire()
    global  num
#    time.sleep(1)
    num+=1
    lock.release()

thread_list = []

for i in range(100):
    t = threading.Thread(target=run,args=('thread-%s'%i,))
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print '------all threads done------'
print "num:",num

