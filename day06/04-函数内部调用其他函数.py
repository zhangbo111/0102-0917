# 内层函数
def func2():
    name = '秀芹大妹子'
    # 查找内层函数的name
    print("内层函数", name)
name = ['张大彪']
# func1表示外层函数
def func1(japen):
    name = japen
    func2()
    print("外层函数：", name)
func1("岗村宁次")
# 查找全局变量的name
print("全局：", name)
'''
1、调用func1，执行func1，遇到func2的调用，
必须先执行完func2才会继续执行func1
2、全局调用func1，只有执行完func1才会继续执行全局变量中的代码
'''














