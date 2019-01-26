import pymongo

# 使用pymongo连接本地mongo数据库
client = pymongo.MongoClient("127.0.0.1", 27017)
print(client, type(client))

# 连接指定的数据库 runoob
db = client.runoob
print(db)

# 查询数据库中的指定集合的数据
result = db.col.find()
print(result, type(result))

# 使用循环获取可迭代对象中的数据
for item in result:
    print(item)

# 往mongo数据库中插入一条数据
data = {"name": "Andy", "age": 19}
db.col.insert(data)
