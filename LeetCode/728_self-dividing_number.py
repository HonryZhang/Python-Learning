# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

def dividing(num):
    if int(num)>10000 or int(num)<=0:
        exit(0)
    result = []
    #flag=True
    for i in range(1,num+1 ):
        flag = True
        L = list(str(i))
        if '0' in L:
            continue
        for j in L:
            if i % int(j)!=0:
                flag = False
        if flag:
            result.append(i)
    print result

num= int(raw_input('num:'))
dividing(num)


def selfDividingNumbers( left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    ret = []
    for i in range(left, right + 1):
        val = i
        flag = 1
        while i:
            remain = i % 10
            if not remain or val % remain != 0:
                flag = 0
                break
            i /= 10
        if flag:
            ret.append(val)
    print ret

selfDividingNumbers(1, 1000)