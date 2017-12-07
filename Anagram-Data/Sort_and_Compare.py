#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

def anagram_2(s1,s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos0 = 0
    mathchs = True

    while pos0 < len(s1) and mathchs:
        if list1[pos0] == list2[pos0]:
           pos0 +=1
        else:
            mathchs = False
    return mathchs

print anagram_2('abcde','edcba')



