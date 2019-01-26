# 打开一个文件 第一个参数是文件的路径
# 第二个参数是执行文件操作的模式
# 第三个参数是文件操作的编码格式
f = open("./1.txt", "r", encoding='utf-8')

# 读取文件到result  (全部文件内容)
# result = f.read()
# print(result)

# 读取一行 一行一行给你
# result1 = f.readline()
# result2 = f.readline()
# print(result1)
# print(result2)

# 读取多行 形成一个列表
result3 = f.readlines()
print(result3)

# 关闭文件
f.close()
