#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import mysql.connector
import datetime

starttime = datetime.datetime.now()
# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='test', port='3309')
cursor = conn.cursor()
# 创建user表:
cursor.execute('DROP TABLE IF EXISTS `user`')
cursor.execute('create table user (id int primary key, sex int , name varchar(20),time timestamp)')
# 插入一行记录，注意MySQL的占位符是%s,无论是数字还是字符串！！！:
for i in range(1, 1000):
    cursor.execute('insert into user (id, name,time) values (%s, %s, %s);',
                   [i, 'Michael' + str(i), datetime.datetime.now()])
# 提交事务:
conn.commit()
cursor.close()
# 修改：
cursor = conn.cursor()
for i in range(1, 4):
    cursor.execute('UPDATE user SET `name` = %s WHERE id <= %s', ['jack', i])
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id < %s', [10])
# 输出结果：
values = cursor.fetchall()
print(cursor.rowcount)
for i in values:
    print(i)
    for j in i:
        print(j)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
endtime = datetime.datetime.now()
print(endtime - starttime)
