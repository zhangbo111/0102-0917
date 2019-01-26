import abc
# 固定写法 指定抽象类的元类
# 没有指定元类不能书写抽象类
# 书写一个抽象类
class User(metaclass=abc.ABCMeta):
    # 属性
    username = ""
    userid = 0
    # 实例方法
    @abc.abstractmethod
    def add(self, name, password):
        pass
    # 类方法
    @abc.abstractclassmethod
    def dele(cls, userid):
        pass
    # 静态方法
    @abc.abstractstaticmethod
    def mod():
        pass
    def find(self):
        print("查找用户操作")
class JXUser(User):
    def add(self, name, password):
        print("添加用户操作")
class HBUser(JXUser):
    @classmethod
    def dele(cls, userid):
        print("删除用户操作")
class MXUser(JXUser):
    @staticmethod
    def mod():
        print("修改用户操作")
# 实例化对象 不是抽象类
user = MXUser()
# 添加操作
user.add('昌镐', '123456')
# 删除操作
MXUser.dele("001")
# 修改操作
user.mod()
# 查找操作
user.find()
