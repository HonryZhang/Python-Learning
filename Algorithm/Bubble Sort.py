#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

data_set = [2,1,24,34,15,67,43,4,9,98,103]

loop_count = 0
'''
for j in range(len(data_set)):
    for i in range(len(data_set)-j-1):
        if data_set[i] > data_set[i+1]:
#            print "i is:",data_set[i]
#            print "i+1 is:",data_set[i+1]
            tmp = data_set[i]
            data_set[i]=data_set[i+1]
            data_set[i+1] = tmp
        loop_count+=1
    print data_set
print data_set

print "Loop Times:",loop_count
'''

for i in range(len(data_set)):
    for j in range(i+1,len(data_set)):
        if data_set[i]>data_set[j]:
            data_set[i],data_set[j] = data_set[j],data_set[i]
    print data_set
print data_set
