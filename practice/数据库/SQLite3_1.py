#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/30 14:49
# 导入SQLite驱动:
import sqlite3
import os


def create():
    # 判断需要创建的数据库是否存在，如果存在则删除，不删除直接创建会报错
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    # conn = sqlite3.connect('test.db')
    conn = sqlite3.connect(db_file)
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user (id, name, score) values(\'1\', \'Lin\', 80)')
    cursor.execute('insert into user (id, name, score) values(\'2\', \'Lqq\', 90)')
    cursor.execute('insert into user (id, name, score) values(\'3\', \'cole\', 83)')
    cursor.execute('insert into user (id, name, score) values(\'4\', \'fanta\', 85)')
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()


def select():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user')
    # cursor.execute('select * from user where id = ?', ('2',))
    cursor.execute('select name from user where score between 83 and 85 order by score desc')
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()


def practice(low, high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select name from user where score between ? and ? order by score desc', (low, high))
    result = cursor.fetchall()
    al = [i[0] for i in result]
    print(al)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create()
    select()
    practice(80, 90)
