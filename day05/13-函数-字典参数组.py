# **表示接收键值对的参数 kwargs表示常用的名称
def yanyu(**kwargs):
    print(kwargs, type(kwargs))

# 什么都不传 kwargs接收的是空字典
yanyu()
# 通过键值对的方式传递 字典参数 等号前面是键 后面是值 用kwargs接收
yanyu(lang1='退一步海阔天空', lang2='狭路相逢勇者胜')

# 练习：声明一个函数 传入3,5,68,9,0,1,2 然后返回他们的和以及平均值







