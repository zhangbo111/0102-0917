print('---test1---')
# 把正常需要执行的代码放入try中 而且是需要捕捉异常的代码
try:
    # 如果找不到文件 就会报错异常
    # 程序一遇到异常就会终止
    print(num)
    f = open('2.txt')

# 遇到 FileNotFoundError这个异常会执行里面的代码
# 如果没有遇到FileNotFoundError则不会执行 遇到其他的异常也不会执行
except FileNotFoundError:
    print('找不到文件', FileNotFoundError)
# 如果NameError没有被捕捉到 则报错 捕捉多个异常
except NameError:
    print('NameError', NameError)
# 捕捉异常之后下面的程序可以正常运行
print('---test2---')




