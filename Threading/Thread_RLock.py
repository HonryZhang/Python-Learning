#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import threading,time


def run0():
    print "running the first function"
    lock.acquire()
    global num0
    num0+=1
    lock.release()
    print '----num0----',num0
    return num0

def run1():
    print "running the second function"
    lock.acquire()
    global num1
    num1+=1
    lock.release()
    print '----num1----', num1
    return num1

def run2():
    lock.acquire()
    res0 = run0()
    print "between run0 and run1...."
    res1 = run1()
    lock.release()
    print res0,res1

if __name__ =='__main__':
    num0,num1 = 0,0
    lock = threading.RLock()
    for i in range(3):
        t = threading.Thread(target=run2,)
        t.start()
while threading.active_count()>1:
    print threading.active_count()
else:
    print "----all functions are executed-----"
    print num0,num1