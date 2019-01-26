class Animal:
    pass
class Demo:
    pass
class Human(Animal, Demo):
    """
    这是类的文档
    Animal是第一个父类
    Demo是第二个父类
    """
    age = 18
    name = '笑笑'
    sex= "男"
    def __init__(self):
        self.hair = '金色'
    def sleep(self):
        print("真想睡到自然醒")
    def hobby(self):
        print("打篮球")

dd = Human()
# 获取类和对象的自身成员
print(Human.__dict__)
print(dd.__dict__)
# 获取类的文档 对象的文档可以用类的文档
print(Human.__doc__)
print(dd.__doc__)
# 获取类名 对象名不可使用这样的方式
print(Human.__name__)
# print(dd.__name__)
# 获取一个类直接继承的类组成的元组
print(Human.__bases__)
# 获取去类的模块名称 当前类直接执行的文件 __main__
print(Human.__module__)
