import abc
# 多态的实现：同一个类的相同方法 可以实现不一样结果
# 设计抽象类 定义规则
class Animal(metaclass=abc.ABCMeta):
    # 吃
    @abc.abstractmethod
    def eat(self):
        pass
    # 睡
    @abc.abstractmethod
    def sleep(self):
        pass
    # 获取食物
    @abc.abstractmethod
    def get_food(self):
        pass

class Dog(Animal):
    def eat(self):
        print("狗粮")
    def sleep(self):
        print("狗窝")
    def get_food(self):
        print("撒娇")

class Cat(Animal):
    def eat(self):
        print("猫粮")
    def sleep(self):
        print("屋顶")
    def get_food(self):
        print("抓老鼠")

class Chick(Animal):
    def eat(self):
        print("鸡粮")
    def sleep(self):
        print("鸡窝")
    def get_food(self):
        print("吃虫子")
class Action:
    def __init__(self, animal_name):
        '''
        :param animal_name: 传过来的动物的对象
        '''
        # 给当前类的对象赋值
        self.animal_name = animal_name
    def eat(self):
        self.animal_name.eat()
    def sleep(self):
        self.animal_name.sleep()
    def get_food(self):
        self.animal_name.get_food()
# 实例化狗类
wangcai = Dog()
# 实例化猫类
tom = Cat()
# 实例化鸡类
zhandouji = Chick()

# 实例化动作类
a = Action(wangcai)
# 调用行为类的对象
a.eat()
a.sleep()
a.get_food()

# 改变行为类当中的动物
b = Action(tom)
b.eat()
b.sleep()
b.get_food()

# 改变行为类当中的动物
c = Action(zhandouji)
c.eat()
c.sleep()
c.get_food()






