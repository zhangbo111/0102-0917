'''
实际问题：台阶问题
到达第八层（最后一层）
f(8) = f(7) + f(6)

f(1) --> 1
f(2) --> 1 + 1 = 1 + f(1) = 2
f(3) --> f(2) + f(1)
f(4) --> f(3) + f(2)
...
f(8) = f(7) + f(6)
推出
f(n) = f(n-1) + f(n-2)
斐波那契数列 0 1 1 2 3 5 8 13 21 34 55 ...
'''
# 练习：使用递归的方式实现我们的斐波那契数列
# 要求声明一个递归函数 传入任何一个数字能打印出
# 例如8 要输出前八个斐波那契数 0 1 1 2 3 5 8 13 21

def feibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    # 当num > 2 时
    return feibo(num - 1) + feibo(num - 2)
# 打印单个的斐波那契数列
# result = feibo(8)
# print(result)
# 循环打印多个斐波那契数列
num = int(input("请输入需要打印的长度："))
for i in range(1, num + 1):
    result = feibo(i)
    print(result, end=' ')




