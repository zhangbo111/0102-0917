# len魔术方法  获取类的所有成员
class Human:
    sex = "女"
    weight = 180
    hobby = "basketball"
    def eat(self):
        print("肚包鸡")
    def drink(self):
        print("广东凉茶")
    # __len__魔术方法
    def __len__(self):
        '''
        触发时机：当对象使用len方法的时候
        返回值：必须是整型
        功能：可以计算成员的个数 也可以做其他的操作
        参数：接收一个self对象
        '''
        # print(Human.__dict__)
        # print("len魔术方法被触发")
        # 声明一个空字典 用于储存没有下划线的键值对
        result = {}
        for k, v in Human.__dict__.items():
            # 过滤掉含有下划线的键值对
            if not (k.startswith("__") and k.endswith("__")):
                result[k] = v
        print(result)
        return len(result)
bys = Human()
# print(bys)
# 想要查看Human类拥有多少个成员（属性，方法）
result = len(bys)
print(result)
