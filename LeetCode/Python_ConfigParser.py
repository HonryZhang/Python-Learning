# !/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Hongrui'


'''
#import ConfigParser, os
# 读取配置文件
cp = ConfigParser.ConfigParser()

cp.read(['settings.cfg'])

#  获取所有defaults section
defaults = cp.defaults()
print 'Defaults:',defaults

#  获取所有sections
sections = cp.sections()
print 'section:',sections


# 判断指定 section 是否存在
has_db = cp.has_section('db')
print has_db

# 获取指定 section 的配置信息，只获取键
options = cp.options('db')
print 'Option:',options

optionsss = cp.options('section_b')
print 'optionsss:',optionsss


# 获取指定 section 的配置信息，获取键值
items = cp.items('db')
print 'items:',items

# 获取指定 section 的配置信息，根据键获取值
db_host=cp.get('db', 'db_host')
db_port=cp.getint('db', 'db_port')
db_user=cp.get('db', 'db_user')
db_pass=cp.get('db', 'db_pass')
db_name=cp.get('db', 'db_name')
db_url=cp.get('db', 'db_url')
print db_host, db_port, db_name, db_user, db_pass

# 使用 DEFAULT section 值
# myvalue=cp.get('db', 'mykey')
# print myvalue

# 添加一个section
cp.add_section('section_c')
cp.set('section_c', 'key1', 'value111')
cp.set('section_c', 'key2', 'value222')
cp.set('section_c', 'key3', 'value333')
cp.set('section_c', 'key4', 'value444')
#cp.write(open("test1.cfg", "w"))

# 移除 option
cp.remove_option('section_c','key4')

# 移除 section
cp.remove_section('section_c')

#cp.write(open("test2.cfg", "w"))
'''
import ConfigParser, os
# 读取配置文件
cp = ConfigParser.ConfigParser()

cp.read(['example.conf'])
#  获取所有sections
sections = cp.sections()
print 'section:',sections

opts = eval(cp.get('host','connList'))

#opts = eval(opts)
print 'opts:',opts
print type(opts)
for opt in opts:
    host_info = []
    #print type(opt)
    server_info = eval(cp.get('information',str(opt)))
    print 'server_info:', server_info
    print type(server_info)