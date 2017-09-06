#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import time
import Queue

#函数里面如果有yield，第一次执行会变成一个生成器，并没有真正执行。等到next的时候才开始执行
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield #执行到此，程序返回。yield被唤醒后也可以接受数据
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    r = con.next()
    r = con2.next()
    n = 0
    while n < 3:
        n += 1
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
        con.send(n) #send的两个作用，唤醒生成器的同时并传递一个值，这个值就是yield接收到的值
        con2.send(n)



if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()