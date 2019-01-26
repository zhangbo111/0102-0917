'''
菱形继承
        动物类
鸟类              人类
        鸟人类
'''
class Animal:
    def say(self):
        print("3.7.动物开始吼叫")
        print("4.8.动物结束吼叫")
class Bird(Animal):
    def say(self):
        print("2.鸟开始歌唱")
        Animal.say(self)
        print("5.鸟结束歌唱")
class Human(Animal):
    def say(self):
        print("6.人类开始唱难念的经")
        Animal.say(self)
        print("9.人类结束唱难念的经")
class BirdHuman(Bird, Human):
    def say(self):
        print("1.鸟人开口说话")
        # 先执行完下面的函数 才可以往下执行
        Bird.say(self)
        Human.say(self)
        print("10.鸟人说完了")
# 实例化对象
andeshen = BirdHuman()
andeshen.say()
