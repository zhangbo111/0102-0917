# 第七步：携带收集参数的装饰器
# 扩展函数
def kuozhan(func):
    # 返回的新的eat函数
    def neweat(*args, **kwargs):
        '''
        :param args: 收集所有非关键字参数
        :param kwargs: 收集所有的关键字参数
        :return: 无
        '''
        print(1, args, kwargs)
        # 扩展功能1
        print("妈妈说：饭前要洗手")
        # 调用基本函数
        func(args, kwargs)
        # 扩展功能2
        print("爸爸说：饭后走一走")
    # 返回新装饰好的函数
    return neweat
# 基本函数
@kuozhan  # eat = kuozhan(eat) = neweat
def eat(args, kwargs):
    '''
    :param args: 接收neweat函数里调用基本函数传来的非关键字参数
    :param kwargs: 接收neweat函数里面调用基本函数传过来的关键字参数
    :return: 无
    '''
    print(2, args, kwargs)
    # 获取参数里面相对应的内容
    name = args[0]
    where = args[1]
    name1 = kwargs["name1"]
    where1 = kwargs.get("where1")
    print("{}在{}吃饭".format(name, where))
    print("{}在{}吃饭".format(name1, where1))

# eat本质是kuozhan函数的neweat 不是基本函数
# eat当中的参数传给kuozhan函数内部的neweat函数 分别用args和kwargs进行了接收
eat("洋哥哥", "小蛮腰", name1="邓哥哥", where1="天堂")
