import pymysql

# 连接数据库和添加数据

conn = pymysql.connect(host='localhost',user='root',password='password',database='pymysql',port=3306)
cursor = conn.cursor()

# insert into user(id,username,age,password) values(2,'bbb',20,'111111')
# sql = """
# insert into user(id,username,age,password) values(10,'bbb',20,'111111')
# """
# cursor.execute(sql)
# conn.commit()


# 灵活添加数据
# sql = """
# insert into user(id,username,age,password) values(null,%s,%s,%s)
# """
#
# username = 'spider'
# age = 21
# password = '123456'
#
# cursor.execute(sql,(username,age,password))
# conn.commit()


# sql函数查找数据
# select username,age from user where id=1
# select * from user
# sql = """
# select username,age from user where id=3
# """


# fetchall()函数查找一条数据，在执行就查找下一条
# sql = """
# select * from user
# """
# cursor.execute(sql)
# while True:
#     result = cursor.fetchall()
#     if result:
#         print(result)
#     else:
#         break


# fetchall()函数所有数据
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)

# fetchmany()函数指定多少条数据
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchmany(2)
# for result in results:
#     print(result)


# 删除数据
# sql = """
# delete from user where id=1
# """
# cursor.execute(sql)
# # 插入，删除，更新都需要执行commit()函数
# conn.commit()


# 更新数据
# sql = """
# update user set username='aa456456' where id=2
# """
# 不写条件会将全部的数据更新
sql = """
update user set username='456fa5s4f56a'
"""
cursor.execute(sql)
# 插入，删除，更新都需要执行commit()函数
conn.commit()



# 关闭连接
conn.close()





