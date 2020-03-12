# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import MySQLdb
dbhost = "localhost"
username = "root"
pwd = "123456"
dbname = "mysql"
# Create your tests here.
def  insertdb(curuser,commonconf,bugconf,storyconf,otherconf,taskstat):
    ##向数据库中插入数据
    db = MySQLdb.connect(dbhost,port=3366,user=username,passwd=pwd,db=dbname, charset='utf8')
    cursor = db.cursor()
    sql = "insert into  qualityplat(username,commonconf,bugconf,storyconf,otherconf,taskstat) values ('"+curuser+"','"+str(commonconf)+"','"+str(bugconf)+"','"+str(storyconf)+"','"+str(otherconf)+"','"+str(taskstat)+"')"

    print sql
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
       print  "insert  success!"
    except:
       # Rollback in case there is any error
       db.rollback()
       print  "insert failed"

def  selectfromdb(username):
    db = MySQLdb.connect(dbhost,port=3366,user=username,passwd=pwd,db=dbname, charset='utf8')
    cursor = db.cursor()
    #sql = "insert into  qualityplat(username,commonconf,bugconf,storyconf,otherconf) values ('"+curuser+"','"+str(commonconf)+"','"+str(bugconf)+"','"+str(storyconf)+"','"+str(otherconf)+"')"
    sql = "select * from  qualityplat where username="+username
    print sql
    curusertask = []
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       results = cursor.fetchall()
       for  row  in  results:
           curtask = {}
           curtask["curtaskid"] = row[1]
           curtask["curcommonconf"] = row[2]
           curtask["curbugconf"] = row[3]
           curtask["curstoryconf"] = row[4]
           curtask["curotherconf"] = row[5]

       print  "select success!"
    except:
       # Rollback in case there is any error
       db.rollback()
       print  "insert failed"

def  connect_two_table():
    """连接两个数据库表2020.3.11数据库练习"""
    db = MySQLdb.connect(dbhost,port=3366,user=username,passwd=pwd,db='daily_practice', charset='utf8')
    cursor = db.cursor()
    sql = "select FirstName,LastName,City,State from  person left join address on person.PersonId=address.PersonId"
    print sql
    curusertask = []
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       results = cursor.fetchall()
       print  "select success!"
    except:
       # Rollback in case there is any error
       db.rollback()
       print  "select failed"

def  second_highest_salary():
    """获取第二高的薪水，没有则返回空2020.3.12数据库练习"""
    db = MySQLdb.connect(dbhost,port=3366,user=username,passwd=pwd,db='daily_practice', charset='utf8')
    cursor = db.cursor()
    sql = "select (select distinct Salary from Employee ORDER BY Salary DESC  LIMIT 1 OFFSET 1) as  SecondHighestSalary"
    print sql
    curusertask = []
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       results = cursor.fetchall()
       print  "select success!"
    except:
       # Rollback in case there is any error
       db.rollback()
       print  "select failed"

if  __name__=="__main__":
    #connect_two_table()
    second_highest_salary()
