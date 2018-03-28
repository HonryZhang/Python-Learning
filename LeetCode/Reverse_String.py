# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'


def reverse_string(str):
    l = list(str)
    for i in range(len(l)/2):
        l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
    str = ''.join(l)
    print str

reverse_string('hello')
