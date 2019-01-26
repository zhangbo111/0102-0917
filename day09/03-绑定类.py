class Human:
    # 属性
    age = 22
    sex = "男"
    name = "莫谋笑"
    def eat(self):
        # 通过类来访问 则self只是一个形参 类必须传递一个实参过来
        print(self)
        print('吃西瓜')
    def drink(self):
        # 通过对象访问 self接收的是当前对象jianXing
        # 可以访问jianXing的所有属性和方法
        # 还可以访问当前类的属性和方法
        print(self.hair)
        print(self.age)
        # self.eat()
        print('和西瓜汁')

    # 绑定类的方法
    def la():
        print("这个时候就不要吃东西了")
    # 绑定类的方法/非绑定类的方法 （取决于怎么用）
    # 既可以对象去访问 也可以类去访问
    def run(arg):
        print("跑步有益身心健康")

# 类访问方法
Human.eat("我是花泽类")

# 通过对象访问方法 不需要传递参数
jianXing = Human()
jianXing.hair = 'black'
jianXing.drink()

# 类来访问绑定类的方法
Human.la()
# 绑定类的方法 不能通过对象去访问 只能通过类来访问
# jianXing.la()

# 类和对象都可以访问 用类去访问的时候就是绑定类的方法
Human.run(1)
# 用对象去访问的时候 就是非绑定类的方法
jianXing.run()
