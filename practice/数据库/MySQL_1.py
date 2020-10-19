#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/10 17:20

import mysql.connector

conn = mysql.connector.connect(user="root", password="root", database="test")

cursor = conn.cursor()

cursor.execute('create table user (id int(4) primary key, name varchar(20))')

cursor.execute('insert into user values (%s, %s)', [1, 'Lin'])

print(cursor.rowcount)

conn.commit()

cursor.close()

cursor = conn.cursor()

cursor.execute('select * from user where id = %s', (1,))

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()