#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

from gevent import monkey
import gevent
import urllib
import  time

def f(url):
    print 'GET:%s'%url
#    request = urllib.Request(url)
    resp = urllib.urlopen(url)
#    resp = urlopen(url)
    data = resp.read()
    print '%d bytes received from %s'%(len(data),url)

urls = [
        'https://www.cnblogs.com/',
        'https://www.suning.com/',
        'https://www.jd.com/',
    ]

time_start = time.time()
for url in urls:
    f(url)
print('同步cost',time.time() - time_start)


async_time_start = time.time()
gevent.joinall(
    [
        gevent.spawn(f, 'https://www.zhihu.com/'),
        gevent.spawn(f, 'https://www.suning.com/'),
        gevent.spawn(f, 'https://www.jd.com/'),
    ]
)
print('异步cost',time.time() - async_time_start)