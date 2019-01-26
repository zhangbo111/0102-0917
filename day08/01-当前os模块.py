import os

# .表示当前路径
print(os.curdir)
# 打开当前路径下的文件
# open('./1.txt')

# ..表示父目录（上一层文件夹）
print(os.pardir)

# f = open('../day07/test03', encoding='utf-8')
# result = f.read()
# print(result)
# f.close()

# 获取代表操作系统的名称
print(os.name)  # poist 表示Linux和Unix的内核名称 nt表示windows

# 获取路径的分割符号
print(os.sep)  # Linux --> /  windows --> \

# 获取文件名和后缀之间的分割符
print(os.extsep)


