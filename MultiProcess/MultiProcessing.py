#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import multiprocessing
import  time,threading

def thread_run():
    print (threading._get_ident())

def run(name):
    time.sleep(2)
    print 'hello',name
    t = threading.Thread(target=thread_run)
    t.start()

if __name__=="__main__":
    for i in range(10):
        p=multiprocessing.Process(target=run,args=('UC %s'%i,))
        p.start()