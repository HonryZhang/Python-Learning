#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import gevent

def fun1():
    print 'A'
    gevent.sleep(2)
    print 'B'

def fun2():
    print 'C'
    gevent.sleep(1)
    print 'D'

def fun3():
    print 'E'
    gevent.sleep(0)
    print 'F'

gevent.joinall([gevent.spawn(fun1),gevent.spawn(fun2),gevent.spawn(fun3)]) # 列表形式