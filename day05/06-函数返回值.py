# 返回值：函数的内部元素给外部使用
def sum_num(num1, num2):
    # num1接收的是12 num2接收的13
    # print(num1, num2)
    # 计算两个参数的和并返回 25
    sum = num1 + num2
    # print(sum)
    # 使用return返回我们需要传入到外面的变量 25
    return sum
# 传入多个实参 需要有相同多的形参进行接收
# 并按照顺序一一对应
# 需要一个变量去接收函数内部返回的值
# sum_result 接收的是函数的返回值 即sum
# 相当于 sum_result = sum_num(12, 13) = sum （sum就是return 后面的变量）
sum_result = sum_num(12, 13)
# 接收函数的返回值并打印
print(sum_result)





