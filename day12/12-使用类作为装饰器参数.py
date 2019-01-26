# 第九步：使用类作为装饰器参数
# 装饰器使用的操作类
class Wish:
    # 绑定类的方法 只有类可以访问
    def before():
        print("饭前洗洗手")

    def after():
        print("饭后走一走")
def outer(cls):
    '''
    :param cls: 接收的是Wish类
    :return:kuozhan函数 （真正的装饰器）
    '''
    # print(1, cls)
    def kuozhan(func):
        '''
        :param func: 基本函数（eat）
        :return:
        '''
        def neweat():
            # 扩展功能1
            cls.before()
            # 基本函数
            func()
            # 扩展功能2
            cls.after()
        # kuozhan函数的返回值
        return neweat
    # outer函数的返回值
    return kuozhan

@outer(Wish)  # eat = kuozhan(eat) = neweat
def eat():
    print("吃饭")

# print(eat)
eat()  # 相当于 neweat() 本质执行的是neweat函数里面的代码
