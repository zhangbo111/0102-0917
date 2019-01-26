# 第五步：携带参数的装饰器  （一）
# 扩展函数
def kuozhan(func):
    # 返回的新的eat函数
    def neweat(name, where):
        '''
        :param name: 接收的是eat的第一个参数 洋哥哥
        :param where: 接收的是eat的第二个参数 小蛮腰
        :return:无
        '''
        print(1, name, where)
        # 扩展功能1
        print("妈妈说：饭前要洗手")
        # 调用基本函数
        func(name, where)
        # 扩展功能2
        print("爸爸说：饭后走一走")
    # 返回新装饰好的函数
    return neweat
# 基本函数
@kuozhan  # eat = kuozhan(eat) = neweat
def eat(name, where):
    '''
    :param name: neweat中调用基本函数传过来的name
    :param where: neweat中调用基本函数传过来的where
    :return: 无
    '''
    print(2, name, where)
    print("{}在{}吃饭".format(name, where))

# eat本质是kuozhan函数的neweat 不是基本函数
# eat当中的参数传给kuozhan函数内部的neweat函数 分别用name和where进行了接收
eat("洋哥哥", "小蛮腰")
