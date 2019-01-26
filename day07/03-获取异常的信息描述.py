# 异常的信息描述是说明你的代码出现什么样的问题 为什么会出现异常
# print(num)

print('---test1---')
# 把正常需要执行的代码放入try中 而且是需要捕捉异常的代码
try:
    print(num)
    f = open('2.txt')
# 捕获异常并同时打印出报错的信息描述 便于查找问题
# 捕获多个异常信息描述 result就是我们的描述信息
except (NameError, FileNotFoundError) as result:
    print("报错信息描述：", result)

# 捕捉异常之后下面的程序可以正常运行
print('---test2---')











