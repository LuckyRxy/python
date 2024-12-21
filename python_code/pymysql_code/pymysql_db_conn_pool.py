# todo: pymysql + DBUtils实现数据库连接池
# prob: 找不到dbutils模块，可能是版本问题
#
# @Time: 2024/12/21 14:36:59
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import pymysql

from dbutils.pooled_db import PooledDB

"""
@todo: 创建连接池
@return: 
"""
pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2, # 最小空闲连接数
    host='localhost',
    user='root',
    password='ren123...',
    database='rxy'
)

# 从连接池中获取连接
connection = pool.connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("Database version:", version)
finally:
    connection.close()
    pass

# 再次获取
connection = pool.connection()

try:
    with connection.cursor() as cursor:
        cursor.execute("select * from employee")
        result = cursor.fetchall()
        for row in result:
            print(f"id:{row[0]}, name:{row[1]}, department_id:{row[2]}, salary:{row[3]}")
finally:
    connection.close()
    pass