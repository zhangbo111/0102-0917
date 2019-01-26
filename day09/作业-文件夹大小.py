import os
# print(os.path.getsize("1.txt"))  # 检测一个文件的大小
# print(os.path.isdir('../day07'))  # 判断是否是文件夹
# print(os.path.isfile('1.txt'))   # 判断是否是文件
# 声明获取文件夹大小的函数 将需要获取的文件夹路径传入进去
def getdirsize(dirpath):
    total = 0
    # print(dirpath)
    # 获取传入的文件夹中所有的文件和文件夹
    allnames = os.listdir(dirpath)
    # print(allnames)
    for i in allnames:
        # 将文件夹中的所有文件或者文件夹拼接成完整路径
        fullnames = os.path.join(dirpath, i)
        # print(fullnames)
        # 获取文件的大小
        if os.path.isfile(fullnames):
            print(fullnames, "--文件")
            total += os.path.getsize(fullnames)
        # 获取文件夹的大小
        else:
            print(fullnames,"--文件夹")
            total += getdirsize(fullnames)
    return total
# 1.89 MB (1,986,413 字节)
total_size = getdirsize('D:\作业')
print("传入的文件夹大小：",total_size)
