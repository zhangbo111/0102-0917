class Human:
    sex = "男"
    ears = 2
    eyes = 2
    color = "black"
    def walk(self):
        print("跑马拉松 真爽")
    def __bool__(self):
        '''
        触发时机：当对象bool(对象)的时候
        返回值：必须是布尔值
        参数：一个self接收类的对象
        功能：自定义返回内容
        '''
        print("bool被触发")
        if self.sex == "男":
            return True
        return False
bb = Human()
result = bool(bb)
print(result)
