'''
在函数最外面声明的变量叫做全局变量
在子程序中声明的变量叫做局部变量
'''
# action = '卧虎藏龙'  # --》全局变量  可以在全局范围内起作用
#
# def wugong():
#     actor = '章子怡'  # --》局部变量 只在函数内部起作用

# action = '卧虎藏龙'  # --》全局变量  可以在全局范围内起作用

# def wugong(act):
#     actor = act  # --》局部变量 只在函数内部起作用
#
# wugong('章子怡')
# # print(actor)  在函数外面不可以调用函数内部的变量 否则会报错

'''
函数内核函数外有相同名称的变量时，
函数内部使用该变量时用的是局部变量，
函数外部使用该变量时 使用的是全局变量
'''
name = '李云龙'
def liangjian(wife):
    # global name  # 可以对name进行修改
    name = wife
    # 就近原则
    print("函数内：", name)

liangjian('小田')
print("函数外：", name)

