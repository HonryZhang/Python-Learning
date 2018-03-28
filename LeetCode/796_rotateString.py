# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

def rotateString(A,B):
    LA= list(A)
    for i in range(len(LA)):
        #print LA[i]
        #LA[i],LA[-1]=LA[-1],LA[i]
        LA.append(LA.pop(0))
 #       print LA
        A = ''.join(LA)
        if A==B:
            print 'oK'

A = 'abcde'
B = 'abced'
rotateString(A,B)

num = [1,2,2]
p = list(set(num))
print p
import collections
num = collections.Counter(num)
for key in num.keys():
    if num[key]==1:
        print key