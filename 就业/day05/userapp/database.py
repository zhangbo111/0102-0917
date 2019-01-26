import redis

c = redis.Redis(host='127.0.0.1', port=6379)

# # # 测试redis是否可用
# c.set("name", "zhang")

# # 导入mongo
# from pymongo import MongoClient
#
# # 连接本地mongo数据库
# conn = MongoClient(host="127.0.0.1", port=27017)
#
# # 连接指定的users数据库
# db = conn.users
# print(db)

# 往数据库里面写入初始化的用户信息
if __name__ == "__main__":
    users = {
        1: {"name": "YSC", "age": 24},
        2: {"name": "YXD", "age": 18},
        3: {"name": "LJB", "age": 30},
        4: {"name": "KDX", "age": 15},
        5: {"name": "YMJ", "age": 12},
        6: {"name": "ZJ", "age": 3}
    }
    for user_id, user in users.items():
        c.hset("users", user_id, str(user))

    # c.lpush("user2", users[0],users[1], users[2], users[3], users[4], users[5])
    # user = ['a', 'b', 'c']
    # for user in users:
    #     c.lpush("user3", user)

    # result = c.lrange("user2", 0, -1)
    # print(result)
    # for i in result:
    #     i = i.decode()
    #     print(i, type(i))





        # print(count)
        # count += 1

    # for user in users:
    #     db.users.insert(user)
    #     print(user, "插入成功")







