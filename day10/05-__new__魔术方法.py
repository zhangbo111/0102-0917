# 实例化魔术方法
class Human:
    age = 19
    sex = "女"
    def __new__(cls, *args, **kwargs):
        '''
        触发时机：实例化创建对象的时候
        功能：控制对象的创建过程
        参数：必须要cls参数接收当前类(Human)
        返回值：可以不返回对象（如果返回则一般是当前类的对象）
        注意：没事没写这个魔术方法
        '''
        # 接收的是当前类
        print(cls)
        # object是所有对象的基类 类可以使用它来创建自己的对象
        print(1, object.__new__(cls))
        # 返回cls（Human类）类的对象
        return object.__new__(cls)
    def __init__(self, name):
        print(name)
    def sleep(self):
        print("每天都要熬夜 太难受了")
    def eat(self):
        print("吃饭时间又到了 最期待的时刻")
# 实例化对象可以触发两个方法
# 1、new方法 创建一个对象(bingbing)
# 2、init方法 初始化对象成员 给对象(bingbing)添加成员
bingbing = Human("喜洋洋")
# Human类的实例bingbing 是__new__方法返回过来的对象
print(2, bingbing)
