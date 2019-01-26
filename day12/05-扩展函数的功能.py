# 第二步：扩展函数
def kuozhan(func):
    '''
    :param func: 是eat函数，把eat函数当做了参数
    :return: 无
    '''
    # 扩展功能1
    print("妈妈说：饭前要洗手")
    # func的调用其实就是eat函数的调用 执行eat函数里面的代码
    func()
    # 扩展功能2
    print("爸爸说：饭后走一走")
# 基本函数
def eat():
    print("吃饭")
# kuozhan(eat)中的eat会传给 func
eat = kuozhan(eat)
# eat函数接收的是kuozhan函数的返回值 （此时还没有实现）
print(eat)