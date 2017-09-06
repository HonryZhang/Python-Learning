#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print "%s is eating... %s"%(self.name,food)


d = Dog("NiuHanYang")
choice = raw_input(">>:").strip()

if hasattr(d,choice):
    print getattr(d,choice)('baox')
#    pass
    func = getattr(d, choice)
    func('bzi')
else:
    setattr(d,choice,bulk) #d.talk = bulk
    func = getattr(d, choice)
    func(d)
