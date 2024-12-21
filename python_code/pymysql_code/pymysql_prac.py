# todo: pymysql练习
#
# @Time: 2024/12/21 12:56:39
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import pymysql 
import yaml

# 读取配置文件
with open('conf.yaml', 'r') as file:
    config = yaml.safe_load(file)

# 从配置文件中获取数据库参数
db_config = config['database']
host = db_config['host']
user = db_config['user']
password = db_config['password']
database = db_config['database']
charset = db_config['charset']
maxconnections = db_config['maxconnections']
mincached = db_config['mincached']
maxcached = db_config['maxcached']

"""
@todo: 建立数据库连接
@return: 
"""
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

"""
@todo: 使用连接对象进行sql查询
@return: 
"""
try:
    with connection.cursor() as cursor:
        cursor.execute("select version()")
        version = cursor.fetchone()
        print("Database version:", version)
finally:
    connection.close()
    pass

"""
@todo: 执行查询语句
@return: 
"""
try:
    with connection.cursor() as cursor:
        cursor.execute("select * from employee")
        result = cursor.fetchall()
        for row in result:
            print(f"id:{row[0]}, name:{row[1]}, department_id:{row[2]}, salary:{row[3]}")
finally:
    connection.close()
    pass

"""
@todo: 执行插入操作
@return: 
"""
try:
    with connection.cursor() as cursor:
        sql = "insert into employee(id, name, department_id, salary) values(%s,%s,%s,%s)"
        cursor.execute(sql,(None,'张三',2,6000))

        connection.commit()
finally:
    connection.close()
    pass

"""
@todo: 执行更新操作
@return: 
"""
try:
    with connection.cursor() as cursor:
        sql = "update employee set salary = %s where name = %s"
        cursor.execute(sql,(8000,"张三"))
        connection.commit()
finally:
    connection.close()
    pass

"""
@todo: 执行删除操作 
@return: 
"""
try:
    with connection.cursor() as cursor:
        sql = "delete from employee where name = %s"
        cursor.execute(sql,("张三"))
        connection.commit()
finally:
    connection.close()
    pass