# 第三步：使用语法糖 （语法）
# 用于扩展基本函数的函数
def kuozhan(func):
    # 扩展功能1
    print("妈妈说：饭前要洗手")
    # 调用基本函数
    func()
    # 扩展功能2
    print("爸爸说：饭后走一走")
    
# 使用语法的方式 传递eat函数给kuozhan函数
# 然后返回的东西用eat接收 （此时没有完成）
@kuozhan   # 相当于eat = kuozhan(eat)
def eat():
    print("吃饭")

# 因为kuozhan函数没有返回值 故eat为None
print(eat)

