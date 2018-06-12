# import math
# import random
# import calendar
# import datetime
# y = datetime.timedelta(days=1)
# print(y)

# print(calendar.month(2018,8))
# num1 =int( input('input num1'))
# num2 =float( input('input num2'))1
# sum = num1 + num2
# print('numOne {0} + numTwo {1} equals: {2}'.format(num1,num2,sum))
# print('-----------')
# num3 = int(input('input numThree'))
# num4 = math.sqrt(num3)
# print('sqrt num3 {0} equals  {1}'.format(num3,num4))
# print(random.randint(1,2))
# x = input('input x\'s value')
# y = input('input y\'s value')
# x,y = (y,x)
# # print('x = {0} , y = {1}'.format(x,y))
# num5 = float(input('input num5 :'))
# if num5 >= 0:
#     if num5 == 0:
#         print('zero')
#     else:
#         print('+')
# else:
#     print('-')
# while True:
#     try:
#         num=int(input('输入一个整数：')) #判断输入是否为整数
#     except ValueError: #不是纯数字需要重新输入
#         print("输入的不是整数！")
#         continue
#     if num%2==0:
#         print('偶数')
#     else:
#         print('奇数')
#     break
# !/usr/bin/python3

# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "root111", "TESTDB1")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
# !/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root111", "TESTDB1")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# # SQL 插入语句
# sql = """ delete from EMPLOYEE  where FIRST_NAME = 'Mac12' """
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # x = 10/0
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
# SQL 查询语句
sql = """SELECT * FROM EMPLOYEE 
       WHERE INCOME > 1000 """
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
