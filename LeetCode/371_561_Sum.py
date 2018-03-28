# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

def getsum(a,b):
    # #print format(3,'b')
    # a_bin = format(a,'b')
    # b_bin = format(b,'b')
    # if len(a_bin)<len(b_bin):
    #     a_bin = a_bin.zfill(len(b_bin))
    # else:
    #     b_bin = b_bin.zfill(len(a_bin))
    # print len(a_bin),len(b_bin),a_bin,b_bin
    # for k,v in enumerate(list(a_bin)):
    #     print k,v
    while a:
        c = a^b
        a = (a&b) <<1
        b = c
    print c

getsum(9,7)

def getsum1(L):
    L = sorted(L)
    tmp=[]
    res = 0
    for i in range(len(L)):
        if i %2 ==0:
            res+=L[i]
    print res
    for j, c in enumerate(L):
        if j %2 ==0:
            tmp.append(int(c))
    print tmp
    print sum(tmp)

    #print sum([int(c) for i, c in enumerate(sorted(L)) if i % 2 == 0])

L=[1,3,4,5,2,5,7,9,21,12,45,25]
getsum1(L)
