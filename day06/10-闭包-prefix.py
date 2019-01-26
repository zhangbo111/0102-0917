# 函数的调用必须是函数名(),不加()表示函数本身
# 调用之后就会执行函数里面的语句
def greeting_conf(prefix):
    # print("外层函数：", prefix)
    # 注意这边不调用不执行
    def greeting(name):
        # 内层可以访问外层函数的变量，但是不能修改
        print("内层函数：", prefix, name)
    # 将函数名进行返回 不是进行调用
    return greeting
# func() = greeting_conf()() = greeting()
# func表示函数调用产生的实例（在闭包中）
func = greeting_conf('hello')
print("function name is ", func.__name__)
print("id of func is ", id(func))

# 就算是传入的参数一样 还是会开辟新的地址
func = greeting_conf('hello')
print("function name is ", func.__name__)
print("id of func is ", id(func))
