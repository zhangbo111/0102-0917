class Email:
    # username = '123'
    password = ''
    def __init__(self):
        self.name = "刘小哥"
    def login(self):
        print("登录操作")
    def logout(self):
        print("退出操作")
    @property
    def username(self):
        '''
        你要获取什么属性就要用什么命名此函数
        # 触发时机：获取被描述的成员属性的时候
        :return: 返回的值用username接收
        '''
        # print('111')
        if len(self.name) == 2:
            return "*" + self.name[-1]
        elif not self.name:
            return "您输入的用户不存在 请重新输入"
        else:
            return self.name[0] + "*" + self.name[-1]

    @username.setter
    def username(self, value):
        '''
        触发时机：当被描述的成员属性被重新赋值的时候
        :param value: 设置成员属性的值
        :return: 无
        '''
        print(value)
        self.name = value
    @username.deleter
    def username(self):
        '''
        触发时机：删除被描述的成员属性的时候
        :return: 无
        '''
        self.name = ''


e = Email()
# 获取指定描述的成员属性
# print(e.username)
# e.username = '李云龙'
# print(e.username)
del e.username
print(e.username)