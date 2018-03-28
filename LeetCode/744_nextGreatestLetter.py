# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

def nextGreatestLetter(letters,target):
    if letters[-1] <= target:
        print letters[0]
        exit()
    low = 0
    high = len(letters)-1
    while low<high:
        mid = (low+high)/2
        if target>=letters[mid]:
            low = mid+1
        else:
            high = mid
    print letters[high],letters[low]
letters = ["c", "f", "j"]
target = "k"
nextGreatestLetter(letters,target)
