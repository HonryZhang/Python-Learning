#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Hongrui'


#jdbc:mysql://localhost:3306/test
#org.gjt.mm.mysql.Driver
import MySQLdb as mdb

con = None
dbname = 'test'

try:

    con = mdb.connect('localhost','root','admin')

    cur = con.cursor()
    cur.execute('show databases')
    cur.execute('drop database '+dbname)
    cur.execute('create database if not exists ' + dbname)
    cur.execute('use '+dbname)
    cur.execute("CREATE TABLE IF NOT EXISTS \
    Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")

    cur.execute('create table if not exists account(accid int(10) Primary key, money int(10))')

    # Insert two lines data

    cur.execute('insert into account (accid,money)values(1,100)')
    cur.execute('insert into account (accid,money)values(2,10)')

    for i in range(30):
        sql = "INSERT INTO Writers(Name) VALUES('zhang%s')"%i
        cur.execute(sql)
    con.commit()
    cur.execute("SELECT * FROM Writers")
    rows = cur.fetchall()
    for row in rows:
        print row
    cur.close()


finally:
    if con:
        con.close()