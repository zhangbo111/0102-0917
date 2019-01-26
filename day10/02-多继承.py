# 多继承
class YeYe:
    def zaocheng(self):
        print('打太极')
    def dance(self):
        print("哎呀 扭到我的腰了 快打120")
class NaiNai:
    def dance(self):
        print("你看我扭得好看不拉")
class BbBa:
    def work(self):
        print("老板 给加点薪水吧")
class MaMa:
    def guang(self):
        print("我的工作就是买买买")
class Son(YeYe, NaiNai, BbBa, MaMa):
    def ask(self):
        print("给我钱 我要打游戏")
xiaoming = Son()
xiaoming.ask()
xiaoming.zaocheng()
# 爷爷拥有第一个dance的方法 所以打印出爷爷的dance方法
xiaoming.dance()
xiaoming.work()
xiaoming.guang()
