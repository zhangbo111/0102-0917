# 第六步：带有返回值的装饰器
# 扩展函数
def kuozhan(func):
    # 内部函数 用于返回给eat
    def neweat():
        # 扩展功能1
        print("妈妈说：饭前要洗手")
        # 调用基本函数 并接收基本函数返回的值 "吃完就睡 一定长胖"
        result = func()
        # 扩展功能2
        print("爸爸说：饭后走一走")
        # 将基本函数返回的值 返回个最后调用neweat的接收返回值的result1
        return result

    # neweat()表示调用   neweat表示函数本身
    # 此时返回的是neweat本身 不是neweat的调用
    return neweat

# 基本函数
@kuozhan  # 相当于eat = kuozhan(eat) = neweat 返回的eat函数必须是新的装饰好之后的函数
def eat():
    print("吃饭")
    return "吃完就睡 一定长胖"

# 此时的扩展之后eat接受到的是返回的neweat
# 本质就是传一个旧的函数进去 返回一个新的函数的过程
print(eat)
# 调用装饰之后的eat函数 也就是neweat函数
# neweat函数的返回值用result接收
# 目的：result接收的是基本函数的返回值 "吃完就睡 一定长胖"
result1 = eat()
print(1, result1)



