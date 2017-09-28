#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
name = ['physics', 'chemistry', 1997, 2000,1, 2, 3, 4, 5, 6, 7,2,4,5,19,1, 2, 3, 4, 5, 6, 7]
first_pos = 0

for i in range(name.count(2)):
    new_list = name[first_pos:]

    next_pos = new_list.index(2) +1
    print "Find:", first_pos+next_pos
    first_pos += next_pos
    
for i in range(len(name)):
    if name[i] ==2:
        print i+1
pos = 0        
for i in range(name.count(2)):
    if first_pos==0:
        pos = name.index(2) +1
    else:
        pos = name.index(2,pos+1 )
    print pos +1
'''
'''
keys = []
value =[]
import re
with open ('D:/Eclipse/Workspace/PythonCase/test.txt','r') as f:
        for line in f:
                res = re.match(r'(.+):\s+(\d+)',line.strip())
                print res.group(1)
                keys.append(res.group(1))
                value.append(res.group(2))
        print keys    
'''
'''
#res = re.match(r'(\w+):\s+(\d+)','Cached:          5021652 kB')
#print res.group(2)
'''

'''
import os
import hashlib
# res = os.popen('dir').read()
# print type(res)
# print res.decode('gbk')

hash = hashlib.md5()
hash.update('name')
hash.update('hx')
print hash.hexdigest()


print os.path.dirname(__file__)
import getpass
user = getpass.getuser()
print user
# passwd = getpass.getpass()
# print passwd

msg = 'get ls dir'
list = msg.split(' ')
print list
ins = "lst_file|%s"%(' '.join(list[1:]))
print ins


# def help(self):
#     print '''
#     command_type    command_instruction
#     help            help
#     get             get remote_filename
#     put             put local_filename
#     exit            exit the system
#     ls              list all the files int the current directory
#     del             del the remote filename
#     cd              cd  the dest_dir
#     '''
#
# print os.path.dirname(__file__)
    


#九九乘法表
'''
def gen(line_cnt):
    for i in range(1,line_cnt+1):
        for j in range(1,i+1):
            m= i*j
            print '%s * %s = %s\t'%(i,j,m)
if __name__ =="__main__":
    gen(9)
'''

#互不相同无重复的数字
# cnt = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 print i*100+j*10+k
#                 cnt +=1
# print cnt

#!/usr/bin/python
#-*- coding:utf-8 -*-

#from math import sqrt
# def number():
#     for i in range(100,201):
#         flag = 1
#         k = int(sqrt(i))
#         for j in range(2,k+1):
#             if i%j ==0:
#                 flag =0
#                 break
#
#         if flag==1:
#             print '%5d\n'%i,
#     b1 = [1, 2, 3]
#     b2 = [2, 3, 4]
#     b3 = [val for val in b1 if val  in b2]
#     print b3
# if __name__ =="__main__":
#     number()

# List = ['1','2','4','2']
# d=[6,5,7,8,9,0]
# b = {}
# b = b.fromkeys(a)
# print b.values()
# c = list(b.keys())
# print c

# a = [1,2,3,4,5,6]
# d=[6,5,7,8,9,0]
# a.append(23)
# a.extend(d)
# print a

# print a+d
# import random
# import string
# a = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
# print a
#
# aList = ['1','2','4','2']
# aList.append( 2009 )
# print "Updated List : ", aList
#
# for i in range(1,10):
#     print '\n'
#     for j in range(1,10):
#         if(i>=j):
#             print '%d*%d=%d' % (i, j, i * j),

#!/usr/bin/python
#-*- coding:utf-8 -*-

# mylist = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9]

# myset = set(mylist)

# print myset

# for item in myset:
#     print item, mylist.count(item)

# for i in range(1,10):
#     print '\n'
#     for j in range(1,10):
#         if(i>=j):
#             print '%d*%d=%d' % (i, j, i * j),
# num = 22
# matrix=[[1,3,15,17,19],
#             [2,4,16,18,22],
#             [3,6,21,22,51],
#             [6,8,22,29,57]]
# last_col_list=[one_list[-1] for one_list in matrix]
# index_list = []
# for i in range(len(last_col_list)):
#     if last_col_list[i] >= num:
#         index_list.append(i)
# print last_col_list
# print index_list
# res_list=[]
# while index_list:
#     one_row=index_list.pop()
# #    print one_row
#     one_list=matrix[one_row]
# #    print  one_list
#     if num in one_list:
#         tmp_str = one_list.index(num)
#         res_list.append(tmp_str)
#         print res_list
#         print 'num exist in the matrix:',num
#
# print 34%10,3%10

def digitCounts(k, n):
    i=j=num=0
    if k==0:
         num=1
    for i in range(n):
        j=i
        while j!=0:
            if j%10==k:
                num+=1
            j=j/10

    print num
digitCounts(2,127)


