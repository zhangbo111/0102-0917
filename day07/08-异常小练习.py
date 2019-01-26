# 小练习：捕获异常
# 1、更改元组 捕获不能更改的异常
# 2、使用下标查询字典的元素 捕获不能获取的异常
# 3、自定义异常：声明一个函数 传入一个列表，列表含有字典
lst = [{"name": "霍华德", "age": 34},{"name": "韦德",'age': 36},{"name":"米切尔","age": 24}]
# 找出年龄大于35岁的老将 并抛出异常 “韦德的年龄大于35，马上要退役了” try except

# # 1、
# try:
#     tup1 = ("靓仔", "靓女", "洒洒水")
#     tup1 += "我稀饭你"
#     print(tup1)
# except Exception as e:
#     print("异常描述信息：", e)

# # 2、
# try:
#     dct = {"name": "韦德",'age': 36}
#     result = dct[0]
#     print(result)
# except Exception as e:
#     print("异常描述信息：", e)

def func(lst):
    print(lst)
    for i in lst:
        try:
            if i['age'] > 35:
                raise Exception('{}的年龄大于35，马上要退役了 一路走好'.format(i['name']))
        except Exception as e:
            print("异常描述信息：", e)

lst = [{"name": "霍华德", "age": 34},{"name": "韦德",'age': 36},{"name":"米切尔","age": 24}]
func(lst)
