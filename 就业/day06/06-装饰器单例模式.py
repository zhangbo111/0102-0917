def Singleton(cls):
    # print(cls)
    # 声明一个空字典 用于存放cls（最初的MyClass）的实例
    instance = {}
    def getinstance():
        # 判断cls在不在instance中 如果不在 则表示第一次 然后创建实例
        # 如果在则直接返回实例就可以
        if cls not in instance:
            # 创建类的实例 并把类的实例存入字典
            # 以类为键 实例为值
            instance[cls] = cls()
        # 第二次来的时候 不用创建 直接返回上次创建好的实例
        return instance[cls]
    return getinstance
@Singleton   # 相当于 MyClass = Singleton(MyClass) = getinstance
class MyClass:
    pass
# 此时的MyClass是Singleton函数的返回值
print(MyClass)
# MyClass() = getinstance() 相当于getinstance的返回值
# a b c d 是同一个返回值
a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()
print(a)
print(b)
print(c)
print(d)

# {cls: instance}

