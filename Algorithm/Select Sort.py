#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'
'''
基本思想
在要排序的一组数中,选出最小（或者最大）的一个数与第1个位置的数交换；然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，依次类推，直到第n - 1
个元素（倒数第二个数）和第n个元素（最后一个数）比较为止。
操作方法：
第一趟，从n 个记录中找出关键码最小的记录与第一个记录交换；
第二趟，从第二个记录开始的n-1 个记录中再选出关键码最小的记录与第二个记录交换；
以此类推.....
第i 趟，则从第i 个记录开始的n-i+1 个记录中选出关键码最小的记录与第i 个记录交换，
直到整个序列按关键码有序。
'''
data_set = [2,1,24,34,15,67,43,4,9,98,103]

loop_count = 0

for i in range(len(data_set)):
    min = i
    for j in range(i+1,len(data_set)-1):
        d = data_set[min]
        if data_set[min]> data_set[j]:
            a = data_set[min]
            b = data_set[i]
            c = data_set[j]
            data_set[min],data_set[j] = data_set[j],data_set[min]
    print data_set
print data_set

