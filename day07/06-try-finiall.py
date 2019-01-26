try:
    # 必须正常生成一个io对象 f  否则下面的finally会报错
    f = open("test")
    print(f, type(f))
    f.read().decode('gbk')
# except Exception as e:
#     print('异常描述信息：', e)
# 如果你有必须要执行的代码 使用finally表示无论前面是否报错 这里必须执行
finally:
    # 无论文件打开和读取是否报错 都要执行关闭文件操作
    f.close()
    print('关闭文件')






