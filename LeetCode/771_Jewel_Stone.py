# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'
import collections
def find_J(J,S):
    sum = 0
    J_dict = collections.Counter(J)
    S_dict = collections.Counter(S)
    for k,v in J_dict.items():
        if S_dict.has_key(k):
            sum+=S_dict[k]
    print sum
    # tmp ={}
    # for i in list(J):
    #     if i in list(S):
    #         tmp[i]= tmp.get(i,0)+1
    # print tmp

find_J('aAbde','aAAbbbccdddeeee')
#find_J('z','ZZ')
