# 可变参数
# 定义一个food函数
def food(haixian):
    # 给可变形参添加一个元素
    haixian.append('小龙虾')
    print(haixian)
# 声明一个列表
lst = ['大鱼']
# 调用并传入一个可变参数
food(lst)
# 查看函数里面的形参的改变会不会影响到外面的实参
# 结论：传入的参数是可变参数时，函数内部的形参做出改变
# 外面的实参也会做出同样的改变
print(lst)










