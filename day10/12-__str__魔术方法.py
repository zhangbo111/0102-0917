# str魔术方法
class ShenZhen:
    tese = "大梅沙 小梅沙"
    gangkou = '蛇口'
    def chanye(self):
        print("毕竟腾讯的总部在这边")
    def waidiren(self):
        print("只要来深圳 就是深圳人")
    # str魔术方法
    def __str__(self):
        '''
        触发时机：print（对象），str（对象）的时候
        返回值：必须返回字符串
        参数：一个self对象
        功能：定义对象转换为字符串的结果
        '''
        print("str魔术方法被触发")
        # 返回的值用longgang去接收
        return self.gangkou
longgang = ShenZhen()
# longgang.chanye()
# 触发str魔术方法 并将 返回值的字符串用longgang去接收 只在print（）的括号里面起作用
# print(longgang)
# 接收完str之后
# longgang.chanye()
# longgang此时的类型还是ShenZhen的对象
# print(type(longgang))
# 触发str的第二种方式
name = str(longgang)
print(name)


