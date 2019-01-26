# 将我们的当期目录移动到指定的位置（上一级）
import sys
sys.path.append("..")
from database import db
# print(db)


# 定义操作mongo库的类
class UserModel(object):

    # 获取单个用户
    @classmethod
    def get(cls, user_id):
        user_info = db.users.find({"user_id": user_id})
        for user in user_info:
            # print(user)
            return user

    # 获取所有的用户信息
    @classmethod
    def get_all(cls):
        # 将所有的用户信息查询出来放入列表当中
        user_list = []
        for user in db.users.find({}):
            del user["_id"]
            user_list.append(user)

        return user_list

    # 创建用户对象
    @classmethod
    def create(cls, name, age):
        # 查询用户信息数量
        user_count = db.users.find().count()
        # 获取user_id最大的文档
        max_user_id_user_info = db.users.find({}).sort("user_id").skip(user_count-1).limit(1)
        for user_info in max_user_id_user_info:
            # 获取文档的最大user_id
            max_user_id = user_info.get("user_id")
            # 在原有的最大user_id 的基础上加1 插入mongo库
            db.users.insert({"user_id": max_user_id + 1, "name": name, "age": int(age)})

    # 修改用户信息
    @classmethod
    def update(cls, user_id, age):
        db.users.update({"user_id": user_id}, {"$set": {"age": int(age)}})

    # 删除用户信息
    @classmethod
    def delete(cls, user_id):
        db.users.remove({"user_id": user_id}, 1)
