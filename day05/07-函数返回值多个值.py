# # 函数返回多个值
# def eat(name1,name2):
#     # print(name)
#     # 将name1和name2 分别传入字典
#     name1_dict = {'name': name1}
#     name2_dict = {'name': name2}
#     # 返回的值是一个元组 其实是省略了小括号
#     return name1_dict, name2_dict
# # name_tuple接收的是一个元组 把向洋和豪斌分别传给name1和name2
# name_tuple = eat('向洋','豪斌')
# # 检查多个返回值返回的类型 它是一个元组
# print(name_tuple,type(name_tuple))

# 练习：声明一个函数，传入两个参数8,3 返回一个元组，
# 元组包含8和3的和，差，乘积，商，取整，取余。最后打印出来
# num1接收的是8 num2 接收的是3
def jisuan(num1, num2):
    # print(num1, num2)
    he = num1 + num2  # 和
    cha = num1 - num2  # 差
    ji = num1 * num2  # 积
    shang = num1 / num2  # 商
    quzheng = num1 // num2  # 取整
    quyu = num1 % num2  # 取余
    # print(he, cha, ji, shang, quzheng, quyu)
    return he, cha, ji, shang, quzheng, quyu
# 调用并传入实参 8和3
# 使用result接收返回的多个元素组成的元组
result = jisuan(8, 3)
print(result)




