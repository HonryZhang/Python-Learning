# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

def reverse(str):
    result = str.split(' ')
    print result
    for i in range(len(result)/2):
        result[i],result[len(result)-1-i] = result[len(result)-1-i],result[i]
    str = ' '.join(result)

    print str

reverse('this is a test script')
reverse('hello smart guy')
a =[3,4,6,5,3]
print reduce(lambda x, y: x+y, [a[x]+(x)%2*3 for x in range(len(a))])