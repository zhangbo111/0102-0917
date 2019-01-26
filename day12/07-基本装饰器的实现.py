# 第四步：基本装饰器的实现
# 扩展函数
def kuozhan(func):
    # 内部函数 用于返回给eat
    def neweat():
        # 扩展功能1
        print("妈妈说：饭前要洗手")
        # 调用基本函数
        func()
        # 扩展功能2
        print("爸爸说：饭后走一走")
    # neweat()表示调用   neweat表示函数本身
    # 此时返回的是neweat本身 不是neweat的调用
    return neweat

# 基本函数
@kuozhan  # 相当于eat = kuozhan(eat) = neweat 返回的eat函数必须是新的装饰好之后的函数
def eat():
    print("吃饭")

# 此时的扩展之后eat接受到的是返回的neweat
# 本质就是传一个旧的函数进去 返回一个新的函数的过程
print(eat)
# 调用装饰之后的eat函数 也就是neweat函数
eat()

# # 扩展之后之后的函数
# def eat():
#     # 扩展功能1
#     print("妈妈说：饭前要洗手")
#     # 调用基本函数
#     print("吃饭")
#     # 扩展功能2
#     print("爸爸说：饭后走一走")






