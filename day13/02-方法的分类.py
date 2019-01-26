class Cat:
    color = "orange"
    name = "小黑"
    sex = "公"
    age = 2
    # 非绑定类的方法/实例方法/对象方法
    def getFish(self):
        '''
        可调用：类，对象
        self:当前类的对象
        '''
        print("如果人类不给饭 我就下海捕鱼")
    # 绑定类的方法
    def say():
        '''
        可调用：类 对象不可调用
        参数：不接受任何参数
        '''
        print("喵喵：今晚很寂寞 我要发情了")

    # 类方法
    @classmethod
    def run(cls):
        '''
        可调用：类,对象
        cls:接收的是当前类
        '''
        print(1, cls)
        print('农村的猫 还是需要抓老鼠的')

    # 静态方法
    @staticmethod
    def jump():
        '''
        可调用：类，对象
        参数：没有传任何的参数
        '''
        print("我是跳高选手 谁敢与我一战")
mimi = Cat()
# 非绑定类的方法、对象方法、实例方法
mimi.getFish()
# 绑定类的方法
Cat.say()
# 类方法
Cat.run()
mimi.run()
# 静态方法
Cat.jump()
mimi.jump()


