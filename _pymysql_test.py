# -*- coding: utf-8 -*-
__author__ = 'Edward'
import pymysql
conn=pymysql.connect(user='root',password='151480',database='test')
cursor=conn.cursor()
cursor.execute('drop table user')
cursor.execute('create table if not exists user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert ignore into  user (id,name) values (%s,%s)',['1','Edward'])
cursor.execute('drop table book')
cursor.execute('create table if not exists book (id varchar(20) primary key,name varchar(20),user_id varchar(20))')
cursor.execute('insert ignore into book (id,name) values (%s,%s)',['1','Edward'])
conn.commit()
cursor.close()
cursor=conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
print(cursor.fetchall())
cursor.close()
conn.close()