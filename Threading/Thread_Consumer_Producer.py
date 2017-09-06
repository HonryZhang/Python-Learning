#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import threading
import Queue

q = Queue.Queue()

def producer():
    for i in range(10):
        q.put("包子-%s"%i)
    print '等待所有的包子被取走'
    q.join()
    print '所有的包子被取走'

def consumer(n):
    while q.qsize()>0:
        print '%s吃了包子%s'%(n,q.get())
        q.task_done()

p = threading.Thread(target=producer,)
p.start()

c1 = consumer('XXX')
