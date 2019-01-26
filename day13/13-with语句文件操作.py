# with语句  可以不写文件关闭操作 自动执行这个操作

# 读取文件
# with open("./1.txt", 'r', encoding='utf-8') as f:
#     result = f.read()
#     print(result)

# # 写入文件 覆盖掉以前的所有内容
# with open("./1.txt", 'w', encoding='utf-8') as f:
#     f.write("恰同学少年\n风华正茂\n书生意气\n挥斥方遒")

# 追加模式  不覆盖掉以前的内容 在原有的基础上添加
with open("./1.txt", 'a', encoding='utf-8') as f:
    f.write("\n作者：毛泽东 字：润之")

