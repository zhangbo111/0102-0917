# 定义描述符类
class Description:
    def __init__(self):
        self.name = '阮先生'
    def __get__(self, obj, cls):
        '''
        触发时机：获取指定描述符描述的成员属性
        self:表示当前描述符类的对象
        :param obj: 是Emali类的对象e
        :param cls: Email类本身
        :return: 返回最终获取到的值 (e.username)
        '''
        # print(0, obj)
        if len(self.name) == 2:
            return "*" + self.name[-1]
        elif not self.name:
            return "用户不存在"
        else:
            return self.name[0] + "*" + self.name[-1]
    def __set__(self, obj, value):
        '''
        触发时机：当指定描述符类描述的成员属性被设置的时候
        self:当前类（Description）的对象
        :param obj:是Emali类的对象e
        :param value: 被描述的成员属性设置的值（斌斌同学）
        :return: 无
        '''
        # print(1, obj)
        # print(2, value)
        self.name = value + "思密达"
        # print(3, self.name)
    def __delete__(self, obj):
        '''
        :param obj: 是Emali类的对象e
        :return: 无
        '''
        self.name = ''
class Email:
    # username 即是Email类的属性 也是Description类的对象
    # username 是指定描述符操作的成员属性
    # 当获取username的时候触发 Description的__get__魔术方法
    # 触发get返回的值（阮*生） 用username接收
    username = Description()
    password = "123456"
    def login(self):
        print("登录操作")
    def logout(self):
        print("退出操作")
# 实例化对象
e = Email()
# 获取对象e的属性
# print(e.username)
# 给指定描述的成员属性设置值
# e.username = '斌斌同学'
# print(e.username)
# 删除指定描述的成员属性
del e.username
print(e.username)
