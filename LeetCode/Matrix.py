#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

'''
Qustion: 有一个m*n整数矩阵，从左到右单调递增，从上到下单调递增，判断一个指定的数是否在此矩阵中？
'''

def matrixSearch(matrix, num):

    #Get the value of the last column
    last_col = [col_list[-1] for col_list in matrix]

    #Compare the number with the value in the last_col
    #Get the row index list
    index_list = []
    for i in range(len(last_col)):
        if last_col[i]>= num:
            index_list.append(i)
    flag = 0
    if index_list:
        for j in range(len(index_list)):
        #Get the row value of the matrix
            row_list = matrix[index_list[j]]

        #Match the value in the row
            if num in row_list:
                row = index_list[j]
                col = row_list.index(num)
                flag = 1
                print 'num %s exists in the matrix:Row:%s,Col:%s'%(num,row,col)

    if flag==0:
        print 'num %s not exists in the matrix.'%num

if __name__=="__main__":
    matrix = [[1, 2, 15, 17, 19],
              [2, 4, 16, 18, 22],
              [3, 6, 21, 22, 32],
              [6, 8, 22, 30, 57]]
    while True:
        num = int(raw_input('Please input a number:>>'))
        matrixSearch(matrix,num)
        