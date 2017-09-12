#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

data_set = [2,1,24,34,15,67,43,4,9,98,103]

loop_count = 0

for i in range(len(data_set)):
    min = i
    for j in range(i+1,len(data_set)-1):
        d = data_set[min]
        if data_set[min]> data_set[j]:
            a = data_set[min]
            b = data_set[i]
            c = data_set[j]
            data_set[min],data_set[j] = data_set[j],data_set[min]
    print data_set
print data_set

