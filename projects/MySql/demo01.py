import pymysql

# 连接数据库

conn = pymysql.connect(host='localhost',user='root',password='password',database='pymysql',port=3306)
cursor = conn.cursor()
cursor.execute('select 2')
result = cursor.fetchone()

print(result)
# 关闭连接
conn.close()
