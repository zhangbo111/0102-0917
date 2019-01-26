# 文件读取操作
class ReadFile:
    def __init__(self, filepath):
        print("=====文件打开====")
        # 给self（file）对象 添加成员
        # 打开文件 生成io文件操作对象 用于读取和关闭文件
        self.fp = open(filepath, encoding='utf-8')
    # 使用self.fp读取文件 并返回
    def read(self):
        print("=====文件读取=======")
        result = self.fp.read()
        return result
    # 当程序完全结束之后 关闭文件
    def __del__(self):
        print("=====文件关闭=====")
        self.fp.close()
# 实例化文件对象
file = ReadFile("./1.txt")
result = file.read()
print(result)
