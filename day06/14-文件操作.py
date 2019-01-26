# 1、打开文件
# 文件路径:必须是字符串 生成一个操作文件的io对象
# 使用的是utf-8编码方式打开文件 此编码格式全世界通用
# gbk表中国的编码格式
f = open('1.txt', encoding='utf-8')
print(f, type(f))

# 2、读取文件
result = f.read()
print(result)

# 3、关闭文件 如果不关闭会造成内存的损耗
f.close()

