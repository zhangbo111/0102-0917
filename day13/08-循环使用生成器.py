# 循环使用生成器 打印出hello
def hello(value):
    print(value)
    # 获取hello的长度
    length = len(value)
    for i in range(length-1, -1, -1):
        print(i, end=' ')
        yield value[i]
hello_gen = hello("hello")
print(hello_gen, type(hello_gen))
# print(next(hello_gen))
# print(next(hello_gen))
# print(next(hello_gen))
for a in hello_gen:
    print(a)

# print([i for i in range(4, -1, -1)])


