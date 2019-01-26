# 单继承
class Biology:
    life = '活的'
    def cell(self):
        print("生物必须有细胞 氨基酸等元素")
# Animal是别的类的父类 也是另外的类的子类
class Animal(Biology):
    age = 80
    def run(self):
        print("动物是会跑的 会动的生物")
class Monkey(Animal):
    hair = '棕色'
    def hobby(self):
        print("打架")
class Jingsihou(Monkey):
    eyes = "炯炯有神"
    def aihao(self):
        print("吃香蕉")
# 实例化Jingsihou类
tuotuo = Jingsihou()
# 访问方法 如果当前类访问不到 则一直找他的父类 直到找到为止
tuotuo.aihao()
tuotuo.hobby()
tuotuo.run()
tuotuo.cell()
# tuotuo.drink()
