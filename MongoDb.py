#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pymongo

conn = MongoClient('localhost',27017)
#conn = MongoClient( 'mongodb://root:admin@192.168.29.79:27107')
#连接数据库，如果没有则自动创建数据库
db = conn.mydb
db.test_set.drop()
#使用test_set集合，没有就自动创建
#db.authenticate("root","admin")
my_set = db.test_set

#插入数据
#insert插入一个列表多条数据不用遍历，效率高
#save需要遍历列表，一个个的插入
my_set.insert({"IPaddr":"192.168.28.100","Username":"root","Passwd":"admin"})
my_set.save({"IPaddr":"192.168.28.101","Username":"root","Passwd":"admin"})

#插入多条数据
hw_info = [{"IPaddr":"192.168.28.102","Username":"root","Passwd":"admin"},{"IPaddr":"192.168.28.111","Username":"root","Passwd":"admin"},{"IPaddr":"192.168.28.112","Username":"admin","Passwd":"admin"}]
users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20},{"name":"wangsu","age":23},{"name":"lldid","age":20}] 
my_set.insert(hw_info)
my_set.insert(users)

#查询数据
for i in my_set.find():
    print i,
print "----------------------"
for i in my_set.find({"Passwd":"admin"}):
    print i,
print ">>>>>>>>>>>>>>>>"
print (my_set.find_one({"IPaddr":"192.168.28.100"}))

#更新数据
my_set.update({"IPaddr":"192.168.28.112"},{'$set':{"Username":"root"}})

#删除数据
#删除name为zhangsan的所有数据
my_set.remove({"name":"zhangsan"})

#删除name为lisi的某个ID
ID = my_set.find_one({"name":"lisi"})["_id"]
print 'ID is:........................',ID
my_set.remove(ID)



