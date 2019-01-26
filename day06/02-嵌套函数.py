name = ['张大彪']
# func1表示外层函数
def func1(japen):
    name = japen
    # func表示内层函数
    def func2():
        name = '秀芹大妹子'
        # 查找内层函数的name
        print("内层函数", name)
    func2()
    # 查找外层函数的name
    print("外层函数：", name)

func1("岗村宁次")
# 查找全局变量的name
print("全局：", name)


