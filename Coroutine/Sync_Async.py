#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import gevent

def task (pid):
    gevent.sleep(0.5)
    print 'Task %s is done'%pid

def sync():
    for i in range(1,10):
        task(i)

def async():
    threads = [gevent.spawn(task,i) for i in range(1,10)]
    gevent.joinall(threads)

print "-----sync-----"
sync()

print ">>>>>async>>>>>"
async()