try:
    num = 100
    print(num)
    # 当前路径
    f = open('test')
# 捕获所有的异常
except Exception as e:
    print('异常描述信息：', e)
# 程序没有报错 则程序执行else
else:
    print('程序正常运行，执行else里面的代码')
