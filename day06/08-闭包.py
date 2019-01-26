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
func = greeting_conf('hello')
print(func)
# 调用内层函数 并传一个参数进去
func('向洋')   # 相当于 greeting("向洋")
func('豪斌')

func = greeting_conf('扣你急哇')
func('谋笑')
func('建鑫')
func('昌镐')
'''
闭包特点：
1、greeting内部访问了non-local的变量prefix，这是允许的
2、greeting_conf函数调用结束之后，prefix延长了生命周期
'''






