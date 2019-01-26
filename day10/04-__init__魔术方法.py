# 初始化方法
import random
class Human:
    color = "yellow"
    age = 18
    # 初始化魔术方法
    def __init__(self, name):
        '''
        触发时机：在实例化对象的时候（但这个方法不是创建对象的方法）
        功能：为self（对象）添加成员，成员不属于类
        参数：必须接收一个self参数 接收的是类的对象
        返回值：无
        '''
        print("哎呀 我被触发了")
        # name接收的参数是隔壁老王 通过实例化对象进行传参的
        print(1, name)
        # 为wbq对象添加成员
        # 添加的成员不属于类 而属于wbq对象
        self.name = name
        self.hair = "自然卷"
        if random.randint(0, 1) == 0:
            self.sex = "男"
        else:
            self.sex = "女"
wbq = Human("隔壁老王")
print(wbq.name)
print("对象：",wbq.__dict__)
print("类：",Human.__dict__)
