# 人类
class Human:
    # 属性
    age = 18
    __sex = "男"
    color = "yellow"
    hair = "black"
    # 方法
    def say(self):
        print('说话')
    def wark(self):
        print('走路')
    # 私有化封装
    def __niao(self):
        print("嘘嘘...")
    # 在类中访问私有化成员
    def demo(self):
        self.__niao()
        print(self.__sex)
zjl = Human()
# 访问公有化成员
print(zjl.age)
print(zjl.color)
print(zjl.hair)
zjl.say()
zjl.wark()
# 私有化成员不可以在类或者对象外的结构中进行访问
# print(zjl.sex)
# zjl.niao()
# 私有化成员可以在类/对象的当前结构中进行访问
zjl.demo()
# 私有化成员 本质就是改了一个名字而已
print(Human.__dict__)
# 如果非要访问 可以使用如下方式 访问 不推荐
# print(zjl._Human__sex)
# zjl._Human__niao()
