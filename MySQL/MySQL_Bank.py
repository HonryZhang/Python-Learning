#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'

import MySQLdb
import sys

class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn

    def check_acct_available(self,accid):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from account where accid= %s'%accid
            cursor.execute(sql)
            print 'SQL:check_acct_available '+sql
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception('Account %s not exists'%accid)
        finally:
            cursor.close()

    def has_enough_money(self,accid,money):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from account where accid=%s and money>%s'%(accid,money)
            cursor.execute(sql)
            print 'SQL:check_money_available'+sql
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception('Account %s doesn\'t have more money'%accid)
        finally:
            cursor.close()

    def reduce_money(self,accid,money):
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money-%s where accid=%s' % (money, accid)
            cursor.execute(sql)
            print('reduce money' + sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception('Account %s failed to get the money' % accid)
        finally:
            cursor.close()

    def add_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = 'update account set money=money+%s where accid=%s' % (money, accid)
            cursor.execute(sql)
            print('Add money' + sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception('Account %s failed to save the money' % accid)
        finally:
            cursor.close()

    def transfer(self, source_accid, target_accid, money):
        ###检测两个账号是否可用
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            ####检测付款人是否有足够的钱
            self.has_enough_money(source_accid, money)
            self.reduce_money(source_accid, money)
            self.add_money(target_accid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__=='__main__':
    source_accid = sys.argv[1]
    target_accid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.connect('localhost', 'root', 'admin','test',charset='utf8')

    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_accid,target_accid,money)

    except Exception as e:
        print 'Issue: '+str(e)
    finally:
        conn.close()






