# 描述符2
class Email:
    # username = '123'
    password = ''
    def __init__(self):
        self.name = "洋哥哥"
    def login(self):
        print("登录操作")
    def logout(self):
        print("退出操作")
    def get_username(self):
        if len(self.name) == 2:
            return "*" + self.name[-1]
        elif not self.name:
            return "您输入的用户不存在 请重新输入"
        else:
            return self.name[0] + "*" + self.name[-1]
    def set_username(self, value):
        # print(1, value)
        self.name = value
    def del_username(self):
        self.name = ''
    # 给username进行描述
    # 1、当获取描述的成员属性时 触发property中的第一个函数 返回的值 用username接收
    # 2、当给描述的成员属性设置值时 触发第二个函数 没有返回值
    # 3、当描述的成员属性被删除的时候 触发第三个函数 没有返回值
    username = property(get_username, set_username, del_username)
# 实例化对象
e = Email()
# 获取指定的描述符描述的成员属性
# print(e.username)
# 给指定的描述符描述的成员属性重新赋值
e.username = "莫哥哥"
# 获取指定的描述符描述的成员属性
print(e.username)
# 删除描述的成员属性
del e.username
print(e.username)






