import pymongo


# 获取连接Mongodb的对象
client = pymongo.MongoClient('127.0.0.1',port=27017)

# 获取数据库(如果没有当前数据库也没关系)
db = client.zhihu

# 获取数据库的集合（MySQL中的表类似）
collection = db.qa

# 写入数据
# collection.insert({'name':'123'})

# 插入数据
# collection.insert_many([
#     {
#         "username":"bbb",
#         "age":18
#     },{
#         "username":"ccc",
#         "age":19
#     }
# ])

# 查找数据(返回游标)
# cursor = collection.find()
# for x in cursor:
#     print(x)

# 获取集合中一条数据(可以指定条件)
# result = collection.find_one({'name':'123'})
# print(result)

# 更新一条数据
# collection.update_one({'username':'ccc'},{'$set':{'username':'aaa'}})

# 更新多条数据（第一个参数是更新那条数据，第二个参数是更新后的数据）
# collection.update_many({'username':'aaa'},{'$set':{'username':'123'}})

# 删除一条数据
# collection.delete_one({'name':'123'})

# 删除多条数据（第一个参数是删除那条数据）
# collection.delete_many({'username':'123'})



