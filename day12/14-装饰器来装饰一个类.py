# 第十一步：装饰器来装饰一个类
def kuozhan(cls):
    '''
    :param cls: 接收的是Human类(被装饰的类)
    :return: newHuman函数
    '''
    # print(cls)
    def newHuman():
        # 给原来的Human添加一些成员属性
        cls.cloth = "漂亮的小裙子"
        cls.hat = "亮绿的绿帽子"
        # self就是result对象
        cls.run = lambda self:print("每天要跑步 我要成为山顶上的男人")

        # cls被装饰的类
        obj = cls()
        # obj是Human类的对象
        # 此时的obj是装饰之后的Human类的对象
        return obj
    return newHuman
@kuozhan   #  Human = kuozhan(Human) = newHuman
class Human:
    '''
    装饰一个类就是给类添加一些功能
    '''
    age = 100
    weight = "100kg"
    def think(self):
        print("我是谁 我从哪里来 我到哪里去")
# 被装饰之后的类的对象
# 相当于 result = Human() = newHuman()
# newHuman() 返回的东西是result
# result就是返回的obj， obj是装饰之后的Human类的对象
result = Human()
# print(1, result)
# print(Human)
# 打印出装饰之后的类的成员属性 以及调用装饰之后类的方法
print(result.age)
print(result.weight)
result.think()
print(result.cloth)
print(result.hat)
result.run()
