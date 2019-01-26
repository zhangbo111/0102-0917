# 第十步：使用类来作为装饰器
class Kuozhan:
    # 接收装饰器的参数 相当于前面outer
    def __init__(self, act):
        self.act = act
        # print(self, act)
    # 制作一个函数 这是真正的装饰器 （kuozhan）
    def __call__(self, func):
        '''
        触发时机：Kuozhan类的对象当做函数使用的时候
        :param func: 基本函数eat
        :return:
        '''
        # print(1, self, func)
        # 将基本函数赋值给当前类的对象
        self.func = func
        return self.neweat

    # 装饰之后的新的eat函数
    def neweat(self):
        # 扩展功能1
        print("老爸说：饭前不要吃水果")
        # 基本函数eat
        self.func()
        # 扩展功能2
        print("老妈说：饭后不要躺尸")

# 1、result = Kuozhan("吃") 相当于实例化 并把“吃”传给__init__函数
# 2、eat = result(eat)  接收的是__call__函数返回的neweat函数
@Kuozhan("吃")
def eat():
    print("吃饭")

# print(eat)
eat()  # 相当于调用neweat
