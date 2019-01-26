class Singleton(object):
    def __new__(cls):
        '''
        cls：接收的是MyClass类
        '''
        # print(cls)
        if not hasattr(cls, "_instance"):
            # 第一次创建实例的时候
            # 创建cls（MyClass）类的对象 进行返回
            # 将创建的实例赋值给cls（MyClass）的属性_instance
            cls._instance = object.__new__(cls)
        # 第二次创建实例的时候 上面if条件不满足 则直接返回上次创建的实例
        return cls._instance
class MyClass(Singleton):
    a = 1
# 实例化a和b两个对象
a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()
# 打印两个对象 看他们两个是否一样
print(a)
print(b)
print(c)
print(d)
'''
没实现单例模式之前
<__main__.MyClass object at 0x0000000001E6B6D8>
<__main__.MyClass object at 0x0000000001E6BB00>
实现单例模式之后
<__main__.MyClass object at 0x000000000244BC50>
<__main__.MyClass object at 0x000000000244BC50>
<__main__.MyClass object at 0x000000000244BC50>
<__main__.MyClass object at 0x000000000244BC50>

注意：
__init__和__new__方法的区别:
__new__是创建一个实例，先被触发
__init__是给这个实例初始化（给它一些初始化的值），这是后触发
'''
