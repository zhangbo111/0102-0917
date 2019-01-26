# 计算阶乘 1 * 2 * 3 * 4 * 5 = 5!
def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)


result = fact(2)  # = num * fact(num-1) = 2 * fact(1)
print(result)  # fact(n)  = num * fact(num -1) = n * fact(n-1)

'''
fact(1) --> 1
fact(2) --> 2 * 1 = 2 * fact(1)
fact(3) --> 3 * 2 * 1 = 3 * fact(2)
...
n > 1
fact(n) --> n * (n-1) * (n-2) * ... * 1 = n * fact(n-1) = n * (n-1) * fact(n-2) = n*(n-1)*...* fact(1)
'''



