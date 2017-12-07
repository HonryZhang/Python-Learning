#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

def anagram_1(s1,s2):
    a_list = list(s2)

    pos0 = 0
    still_ok = True

    while pos0<len(s1) and still_ok:
        pos1 = 0
        found = False

        while pos1 < len(a_list)and not found:
            if s1[pos0] == a_list[pos1]:
                found = True
            else:
                pos1 = pos1+1
        if found:
            a_list[pos1] = None
        else:
            still_ok = False
        pos0 = pos0+1
    return  still_ok

print (anagram_1('abcd','dcba'))