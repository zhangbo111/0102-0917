import test01
# import就是导入的意思 是导入模块的一种方式
# 一般放在顶行  导入的模块后缀不要
# 获取模块中的函数 模块名.函数名
print(test01.print_fun.__name__)
# 调用模块中的函数
result = test01.print_fun("猴啥类")
print(result)
"""
def print_fun(a):
    print("hello world 雷吼")
    return a
"""
