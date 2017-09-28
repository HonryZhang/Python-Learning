#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

'''
求数字出现的次数？

   a.求1~2593中数字 5 出现的次数？ 比如555，数字5算出现3次。

   b.求 1~N中，数字x (0~9) 出现的次数
'''

'''
Input k: the target number
Input n: the target digit
Output: the total times appeared in the list
'''
def digitCounts(k,n):
    t_count = 0  #define the total count of digit n in the list
    n_count = 0  #define the count of digit n in the singe loop
    index = 0    #define the location of digit n
    p_value = k
    while p_value:
        if p_value%10>n:  #get the single digit count
            n_count = int(p_value/10+1)*(10**index)
        if p_value%10==n: #get the 10th digit count
            n_count = int(p_value/10)*(10**index)+ k%(10**index)+1
        if p_value%10<n:  #get the 100th digit count
            n_count = int(p_value/10)*(10**index)
        t_count +=n_count
        p_value = p_value/10
        index=+1

    print 'the total count of number %s in the list is %s'%(n,t_count)

if __name__=="__main__":
    while True:
        value = int(raw_input('Please input a target value:>>'))
        number = int(raw_input('Please input a digit:>>'))
        if value>0 and number >=0 and number <10:
            digitCounts(value,number)
        else:
            print 'Exited.Please check your input. the target value must be a positive integer and the number must between 0 and 9 '
            break


'''
Test Cases:
TC_1:Input an invalid target number:0
Expected Result:program outputs 0

TC_2:Input an invalid digit which is larger than 9 or is a negtive number
Expect Result: program exited and print correct message

TC_3:Input a special value of the single digit 0
Expect Result: program outputs the correct count

TC_4:Input a negtive value of target
Expect Result: program exited and print correct message
'''