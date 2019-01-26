import os

# 获取当前的工作目录
path = os.getcwd()
print(path)

# 绝对路径是从盘符开始进行查找 相对路径是当当前文件开始
os.chdir('D:\python基础\python课程\day06')
# 获取当前的改变之后的工作目录
new_path = os.getcwd()
print(new_path)

# 获取指定目录下面的所有文件和文件夹组成的列表
path_list = os.listdir('D:\python基础\python课程')
print(path_list)

# 在指定的目录下创建文件夹 没有返回值
# os.mkdir('D:\python基础\python课程\day08')

# 递归创建空的文件夹 没有返回值
# os.makedirs('D:\python基础\python课程\day07\c\d')

# 移除一个空目录
# os.rmdir('D:\python基础\python课程\day07\c\d')

# 递归删除所有的空目录 不是空目录不删除
# os.removedirs(r'D:\python基础\python课程\day07\c\d\e')

# 将文件或者文件夹重新命名
# os.rename(r'D:\python基础\python课程\day07\test',r'D:\python基础\python课程\day07\test03')

# 查看文件或者文件夹的详细信息 只能用绝对路径
# info = os.stat(r'D:\python基础\python课程\day07\test03')
# print(info)

# 获取系统的环境变量
result = os.getenv("PATH")
print(result)
result_list = result.split(';')
for i in result_list:
    print(i)

# exit() 表示退出当期的执行环境
