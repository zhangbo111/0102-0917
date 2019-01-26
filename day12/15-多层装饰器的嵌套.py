# 第十二步：多层装饰器的嵌套
def kuozhan2(func):
    '''
    :param func: neweat
    :return: neweat1
    '''
    def neweat1():
        print("洗手之前 打篮球")
        func()
        print("散步之后 洗个澡")
    return neweat1

def kuozhan1(func):
    def neweat():
        print("饭前洗手")
        func()
        print("饭后散步")
    return neweat


@kuozhan2   #  neweat = kuozhan2(neweat) = neweat1
@kuozhan1   #  eat = kuozhan1(eat) = neweat = neweat1
def eat():
    print("吃饭")
# 走完所有的装饰器再走下面的调用
# eat（） = neweat1（）
eat()

# # eat = neweat
# def neweat():
#     print("饭前洗手")
#     print("吃饭")
#     print("饭后散步")




