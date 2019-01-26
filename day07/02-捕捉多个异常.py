print('---test1---')
# 把正常需要执行的代码放入try中 而且是需要捕捉异常的代码
try:
    # 如果找不到文件 就会报错异常
    # 程序一遇到异常就会终止
    print(num)
    f = open('2.txt')

# 可以通捕获两个异常 只要有一个异常符合就会运行except里面的代码
except (NameError, FileNotFoundError):
    print('异常处理')

# 捕捉异常之后下面的程序可以正常运行
print('---test2---')









