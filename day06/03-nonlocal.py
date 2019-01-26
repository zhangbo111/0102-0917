name = ['张大彪']
# func1表示外层函数
def func1(japen):
    # global name
    name = japen
    # func表示内层函数
    def func2():
        # 把外层函数（不是全局）的name 声明可以在此函数中重新赋值
        nonlocal name
        name = '秀芹大妹子'
        # 查找内层函数的name
        print("内层函数", name)
    func2()
    # 查找外层函数的name
    print("外层函数：", name)
func1("岗村宁次")
# 查找全局变量的name
print("全局：", name)









