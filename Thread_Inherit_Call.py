#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import  threading
import  time

class MyThread(threading.Thread):
    def __init__(self,num,sleep_time):
        self.num = num
        self.sleep_time = sleep_time
#        super(MyThread,self).__init__()
        threading.Thread.__init__(self)

    def run(self):
        print "running task:",self.num
        time.sleep(self.sleep_time)
        print "task done",self.num
t1 = MyThread("t1",2)
t2 = MyThread("t2",5)

# t1.run()
# t2.run()

t1.start()
t2.start()

t1.join()
t2.join()
print "all threads done..."