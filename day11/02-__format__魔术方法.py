# format魔术方法
class Human:
    age = 88
    hobby = "羽毛球"
    sex = "女"
    name = "西门大官人"
    def lang(self):
        print("123")
    def drink(self):
        print("茅台喝不起")
    def __format__(self, arg):
        '''
        触发时机：当字符串.format(对象)的时候触发
        参数：一个接收self类的对象， 第二个参数传递{}里面的内容 必须传
        功能：设置的内容 可以作为format里面的参数 自定义格式化字符串
        :param arg: #^10
        :return: 自定义放回值 返回的内容 放在字符串的{}  必须是字符串
        '''
        print(self, arg)
        # 将arg（限定符）进行分开
        flag1 = arg[0]
        flag2 = arg[1]
        # 字符串切割完后是字符串 需要转换为整型
        flag3 = int(arg[2:])
        print(flag1, flag2, flag3)
        # < 左对齐  > 右对齐  ^ 中间对齐
        if flag2 == "<":
            result = self.name.ljust(flag3, flag1)
        elif flag2 == ">":
            result = self.name.rjust(flag3, flag1)
        else:
            result = self.name.center(flag3, flag1)
        print(result)
        return result
# 实例化对象
xmq = Human()
str1 = "{}勾搭潘经理"
result = str1.format(xmq)
print(result)
