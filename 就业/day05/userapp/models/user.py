# 声明一个与数据库交互的类
class UserModel(object):
    # 基于内存存储 声明我们的初始用户
    users = {
        1: {"name": "YSC", "age": 24},
        2: {"name": "YXD", "age": 18},
        3: {"name": "LJB", "age": 30},
        4: {"name": "KDX", "age": 15},
        5: {"name": "YMJ", "age": 12},
        6: {"name": "ZJ", "age": 3}
    }

    # 获取单个用户
    @classmethod
    def get(cls, user_id):
        return cls.users[user_id]

    # 获取所有用户
    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    # 创建一个新用户
    @classmethod
    def create(cls, name, age):
        user = {"name": name, "age": age}
        # 获取原来的内存用户列表的最大id, 并且给它加1
        max_id = max(cls.users.keys()) + 1
        # 添加用户
        cls.users[max_id] = user

    # 修改用户信息
    @classmethod
    def update(cls, user_id, age):
        cls.users[user_id]["age"] = age

    # 删除用户信息
    @classmethod
    def delete(cls, user_id):
        if user_id in cls.users:
            return cls.users.pop(user_id)
