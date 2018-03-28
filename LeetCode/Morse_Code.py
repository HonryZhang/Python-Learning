# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'
import collections
lower_char = [chr(i) for i in range (97,123)] #打印26个小写字母
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
morse_dict={}
for i in range(len(lower_char)):
    morse_dict[lower_char[i]]=morse_code[i]
#print morse_dict


result = {}
wanted=[]
heheda={}
words = ["gin", "zen", "gig", "msg","items","test","ooz","tqwd","same","qwoc"]
for word in words:
    temp = ''
    word_list = list(word)
    for char in word_list:
        #if morse_dict.has_key(char):
        temp += morse_dict[char]
    result[word] = temp
#print temp
#print result

count = 0
for k,v in result.items():
    heheda[v]= heheda.get(v,0)+1  #判断 value 是否存在，如果已经存在，则个数加1

for v in heheda.values():
    wanted.append(v)
print max(wanted)


