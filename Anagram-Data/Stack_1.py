#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def push (self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def check(self):
        return self.items

def base_converter(number,base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while number >0:
        rem = number%base
        rem_stack.push(rem)
        number = number//base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string+digits[rem_stack.pop()]
    return new_string

print (base_converter(25,2))
print (base_converter(2225,16))
print (base_converter(2225,10))
