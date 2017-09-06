#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import  threading
import time

#定义每个线程要执行的操作
def run(n):
    print "task:",n
    time.sleep(2)
    print "task done",n

start_time = time.time()
thread_list = []

if __name__ =="__main__":
    for i in range(30):
        t1 = threading.Thread(target=run, args=("thread-%s"%i,)) # 生成一个实例
        t1.setDaemon(True) # 把当前线程设置为守护线程
        t1.start()
        thread_list.append(t1)
#for t in thread_list:
#    t.join() #循环线程实例列表，等待所有线程执行完毕

#获取线程名
#   print (t1.getName())
time.sleep(3)
print '-------all threads done--------',threading.current_thread(),threading.active_count()
print "cost:",time.time()-start_time