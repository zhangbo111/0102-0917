# 第八步：有外层函数的携带参数的装饰器 装饰多个基本函数的装饰器（二）
def outer(arg):
    '''
    outer:装饰器的外层函数 并不是装饰器函数
    功能：可以接收参数 根据参数的不同 使用同一个kuozhan装饰器
        返回不一样的装饰后的函数
    :param arg: 调用outer传过来的参数 用于判断
    :return: kuozhan函数（装饰器）
    '''
    print("arg:", arg)
    def kuozhan(func):
        '''
        kuozhan：真正的装饰器函数
        :param func: 基本函数 根据传传过来的参数不同 func接收的就不同
        :return: 根据arg决定
        '''
        def neweat():
            # 扩展功能1
            print("妈妈说：饭前要洗手")
            # 调用eat基本函数
            func()
            # 扩展功能2
            print("爸爸说：饭后走一走")
        def newdrink():
            # 扩展功能1
            print("喝酒前来喝一点牛奶")
            # 调用drink基本函数
            func()
            # 扩展功能2
            print("喝完酒就不要开车了")
        # 根据arg不同 返回不一样的装饰函数
        if arg == "喝":
            return newdrink
        elif arg == "吃":
            return neweat
    # outer函数的返回值
    return kuozhan

result = outer("吃")  # result = outer("say) = kuozhan
# print(1, result)   # result 就是kuozhan函数
@result     # eat = result(eat) = kuozhan(eat) = neweat
def eat():
    print("吃饭")
eat()
# print(eat)

@outer("喝")  #  1、result = outer("喝")  把喝传给 arg 2、相当于 drink = result(drink) = kuozhan(drink) = newdrink
def drink():
    print("喝白兰地")

# 就是kuozhan装饰器函数里面的newdrink
drink()

