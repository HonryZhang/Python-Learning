#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34
    gr2.switch()

def test2():
    print 56
    gr1.switch()
    print 78
    gr1.switch()

gr1 = greenlet(test1) #启动一个携程
gr2 = greenlet(test2)
gr1.switch() #手动切换函数，类似于yield的next