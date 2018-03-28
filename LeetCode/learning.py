# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

# import collections
#
# str = 'abcderabcdsdabcdf'
#
# d = collections.defaultdict(int)
# l = ans = 0
# for i,c in enumerate(str):
#     print 'iiiiii',i
#     while l>0 and d[c]>0:
#         d[str[i-1]] -=1
#         l-=1
#     d[c]+=1
#     print 'dddddd:',d[c]
#     l+=1
#     print 'llllll:',l
#     ans = max(ans,l)
# print 'aaaaa:',ans

'''
def max_substr(string):
    s_list = [s for s in string]
    string = '#' + '#'.join(s_list) + '#'
    max_length = 0
    length = len(string)
    for index in range(0, length):
        r_length = get_length2(string, index, max_length)
        if max_length < r_length:
            max_length = r_length
    return max_length

def get_length2(string, index, max_length):
    # 基于已知的最长字串求最长字串
    # 1.中心+最大半径超出字符串范围, return
    r_ = len(string)
    if index + max_length > r_:
        return max_length

    # 2.无法超越最大半径, return
    l_string = string[index - max_length + 1 : index + 1]
    r_string = string[index : index + max_length]
    if l_string != r_string[::-1]:
        return max_length

    # 3.计算新的最大半径
    result = max_length
    for i in range(max_length, r_):
        if index-i >= 0 and index+i < r_ and string[index-i] == string[index+i]:
            result += 1
        else:
            break
    return result - 1

if __name__ == "__main__":
    result = max_substr("35534323553413435534fsdf35534")
    print result

'''

'''
def lengthOfLongestSubstring(s):
    # write your code here
    res = 0
    if s is None or len(s) == 0:
        return res
    d = {}
    tmp = 0
    start = 0
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        tmp = i - start + 1
        d[s[i]] = i
        res = max(res, tmp)
    return res
if __name__ == "__main__":
    result = lengthOfLongestSubstring("35534323553413435534fsdf35534")
    print result

'''
# from collections import Counter
#
# def findsubString(str):
#     mlist=[]
#     reg=left = ''
#     for l in range(len(str)/2,len(str)):
#         print 'llllllll',l
#         for i in range(len(str)/l,0,-1):
#             print 'iiiiiii:',i
#             reg = str[:l+1]
#             print 'reg is:',reg
#             left=str[l+1:]
#             print 'left is:',left
#             if reg in left:
#                 mlist.append(reg)
#     return Counter(mlist)
#
#
# if __name__ == "__main__":
#     result = findsubString("axasdbcffabc7fbcffabc")
#     print result

# def find_longest_no_repeat_substr(one_str):
#     '''''
#     找出来一个字符串中最长不重复子串
#     '''
#     res_list = []
#     length = len(one_str)
#     for i in range(length):
#         tmp = one_str[i]
#  #       print 'tmp:',tmp
#         for j in range(i + 1, length):
#             if one_str[j] not in tmp:
#   #              print 'jjj:',one_str[j]
#                 tmp += one_str[j]
#             else:
#    #             print 'xxxxxjjj:',one_str[j]
#                 break
#         res_list.append(tmp)
#     #res_list.sort(lambda x, y: cmp(len(x), len(y)))
#     print res_list
#     return res_list[-1]
#
#
# if __name__ == '__main__':
# #    one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
# #    for one_str in one_str_list:
#     one_str = '120135435'
#     res = find_longest_no_repeat_substr(one_str)
#     print '{0}最长非重复子串为：{1}'.format(one_str, res)

#s = 'axasdbcffabc7fbcffabc'
#print [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]
res = {}
def findstr(str):
    for i in range(len(str)-3):
        k = i
        str1 = str[i:i+2]
        str2 = str[i+2:]
        while str1 in str2:
            cnt = 1
            tmp = str2
            while str1 in tmp:
                cnt+=1
                tmp = tmp[tmp.index(str1)+len(str1):]
            if not res.has_key(str1):
                res[str1]=cnt
            k+=1
            str1 = str[i:k+2]
            str2 = str[k+2:]
    return res

if __name__=='__main__':
    res = findstr('abcabcabc')
    print res.keys()

 #   longest_key = sorted(res.keys(),key = lambda x:len(x))[-1]
 #   print longest_key+':'+ str(res[longest_key])







