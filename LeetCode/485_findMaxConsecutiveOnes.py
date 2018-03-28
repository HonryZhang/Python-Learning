# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

#print(format(7634,'b'))

def findMaxConsecutiveOnes(num):
    print(format(num, 'b'))
    num_list = list(format(num,'b'))
    res = []
    count = 0
    for i in range(len(num_list)):
        if int(num_list[i])==1:
            count+=1
        elif count!=0:
            res.append(count)
            count=0

    print max(res)

num = 734
findMaxConsecutiveOnes(num )


