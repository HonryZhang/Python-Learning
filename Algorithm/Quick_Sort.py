#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

def quick_sort(lists,left,right):
    if left>=right:
        return lists
    key = lists[left]
    print 'key is:',key
    low = left
    high = right

    while left<right:
        while left<right and lists[right]>=key:
            k1 =  lists[right]
            right-=1
        lists[left] = lists[right]
        while left<right and lists[left]<=key:
            k2 =  lists[left]
            left+=1
        lists[right] = lists[left]

    lists[right] = key
    print lists

    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)

    return lists

if __name__=="__main__":
    lists = [2,1,24,34,15,67,43,4,9,98,103]
    List = quick_sort(lists,0,len(lists)-1)
    print "result list is:",List
