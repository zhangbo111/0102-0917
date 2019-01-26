import sys
sys.path.append("..")
# from models.user import UserModel   # 基于内存的
# from models.mongo_user import UserModel   # 操作mongo数据库的
from models.redis_user import UserModel   # 操作redis数据库
import tornado.web
from tornado.escape import json_encode

# 测试导入时候成功
# print(UserModel.users)


# 操作获取单个用户的类(处理接口的类)
class UserHandler(tornado.web.RequestHandler):

    # get 方法获取单个用户
    def get(self, user_id):
        '''
        :return: 如果没有找到用户信息，则捕获KeyError 404
        '''
        # print(user_id)
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)
        # del user["_id"]
        # print(user)
        self.write(user)

    # 修改用户信息
    def put(self, user_id):
        age = self.get_argument("age")
        # 调用模型类修改用户信息
        UserModel.update(int(user_id), age)
        # 修改成功，定义返回的信息
        resp = {"status": True, "msg": "update success"}
        self.write(json_encode(resp))

    # 删除用户信息
    def delete(self, user_id):
        print(user_id)
        UserModel.delete(int(user_id))
        # 定义删除成功成功后的提示信息
        resp = {"status": True, "msg": "delete success"}
        self.write(json_encode(resp))


# 操作多个用户的类
# 为什么需要写两个类 因为这两个类 一个是需要传参的 另一个不需要
# 本质上是两个不一样的路由 所以需要两个不一样的类
class UserListHandler(tornado.web.RequestHandler):

    # 获取所有的用户信息
    def get(self):
        # 返回的是含有字典的列表
        users = UserModel.get_all()
        # 将users序列化为一个json字符串
        users = json_encode(users)
        self.write(users)

    # 创建新用户信息
    def post(self):
        # post请求接收参数
        name = self.get_argument("name")
        age = self.get_argument("age")
        # 传递给模型层 进行创建用户信息
        UserModel.create(name, age)
        # 如果创建成功 返回创建成功的提示信息
        resp = {"status": True, "msg": "create success"}
        self.write(json_encode(resp))
