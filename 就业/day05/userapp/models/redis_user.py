import sys
sys.path.append("..")
from database import c


# 定义操作mongo库的类
class UserModel(object):

    # 获取单个用户
    @classmethod
    def get(cls, user_id):
        user = c.hget("users", user_id)
        # 将bytes类型转换为字符串
        user = user.decode()
        # 将字符串转换为字典 进行返回
        user = eval(user)
        return user

    # 获取所有用户
    @classmethod
    def get_all(cls):
        users = c.hgetall("users")
        # print(users, type(users))
        users_dict = {}
        for user_id, user_info in users.items():
            # 将bytes类型转换为字符串
            user = int(user_id.decode())
            user_info = eval(user_info.decode())
            # print(user, type(user))
            # print(user_info, type(user_info))
            users_dict[user] = user_info
        return users_dict

    # 创建用户对象
    @classmethod
    def create(cls, name, age):
        users = c.hgetall("users")
        lst = []
        # 将所有的user_id添加进lst中
        for user_id, user_info in users.items():
            # 将bytes类型转换为字符串
            user_id = int(user_id.decode())
            lst.append(user_id)
        # 求出最大的id
        max_id = max(lst)
        # print(max_id)
        # 在原有的最大id上加1  进行插入
        c.hset("users", max_id+1, str({"name": name, "age": age}))

    # 修改用户信息
    @classmethod
    def update(cls, user_id, age):
        # 通过user_id获取指定的值
        user = c.hget("users", user_id)
        # 转换为字典
        user = eval(user.decode())
        # 将字典中的age修改
        user['age'] = age
        # 从新给user_id赋一个修改后的值
        c.hset("users", user_id, str(user))

    # 删除用户信息
    @classmethod
    def delete(cls, user_id):
        print(user_id)
        c.hdel("users", user_id)
