# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'

import collections
def getminWindow(source, target):
    score = 0
    wanted = collections.Counter(
        target)  # get the char count in the target string
    start, end = 0, len(source)
    tmp = {}  # define a temp dictionary, the key is the char, the value is the count
    tmp_list = collections.deque(
        [])  # get the matched char index
    for index, char in enumerate(source):
        if char in wanted:
            tmp_list.append(
                index)  # 获取字符的索引
            tmp[char] = tmp.get(char,0) + 1  # 如果字符不存在新的字典中，则加入并且 value+1,如果已经存在，value 直接+1
            # print tmp.get(c,0)
            # print d
            print 'tmp_dict', tmp
            print 'tmp_list', tmp_list
            if tmp[char] <= wanted[char]:
                print int(tmp[char])  #
                print int(wanted[char])
                score += 1  # score的值匹配 target的长度
            print tmp_list[0]
            print source[tmp_list[0]]
            print tmp[source[tmp_list[0]]]
            print wanted[source[tmp_list[0]]]
            while tmp_list and tmp[source[tmp_list[0]]] > wanted[source[tmp_list[0]]]:
                tmp[source[tmp_list.popleft()]] -= 1
                print tmp
                print tmp_list
            if score == len(target) and tmp_list[-1] - tmp_list[0] < end - start:
                start, end = tmp_list[0], tmp_list[
                    -1]  # return the matched index
    print  source[start:end + 1]
    print tmp_list