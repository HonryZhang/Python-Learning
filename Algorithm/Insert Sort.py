#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

List = [2,1,24,34,15,67,43,4,9,98,103]

for i in range(1,len(List)):
    tmp = List[i]
    j = i-1
    while j>=0:
        k = List[i]
        v = List[j]
        if tmp<List[j]:
            List[j+1]=List[j]
            List[j]=tmp
        print List
        j-=1
print List