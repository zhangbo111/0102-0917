'''
n < 10
return n
n >= 10
12 = 1 + 2 = 12 // 10 + 12 % 10
123 = 1 + 2 + 3 = 12 + 3
1234 = 1 + 2 + 3 + 4 = 123 + 4
...
f(n) = f(n // 10) + f(n % 10)
'''
# 所有的递归需要 求出递归公式才可以 使用递归的方式
def func(num):
    if num < 10:
        return num
    else:
        return func(num // 10) + func(num % 10)
# 传过去的参数要转化为整型
num = int(input('请输入任意的数字：'))
result = func(num)
print(result)




