#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import os
from multiprocessing import Process


def info(title):
    print(title)
    print('module name:', __name__)
 #   print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1m function f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('main process line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
