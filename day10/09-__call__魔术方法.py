# call魔术方法
class Human:
    sex = "男"
    height = 180
    def eat(self):
        print("就知道吃")
    def __call__(self, *args, **kwargs):
        '''
        触发时机：当类的对象当做函数调用的时候
        参数：至少一个self对象
        功能：简化操作
        返回值：根据程序决定
        '''
        print("call被触发了")
        return "hello 波叔"
wxb = Human()
# 对象当做函数调用 可以接收call函数的返回值
result = wxb()
print(1, result)



