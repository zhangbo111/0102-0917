class LiuBei:
    # 属性
    familyName = "刘"
    firstName = "备"
    sex = "男"
    money = "$100"
    country = "蜀国"
    __wife = ("甘夫人","糜夫人","孙尚香")

    # 方法
    def say(self):
        print("险些损我一员大将 怒摔阿斗")

    # 非绑定类的方法
    def drink(self):
        print(self)
        print("大碗喝酒 大块吃肉")

    def walk(self):
        print("饭后走一走 活到九十九")

    # 绑定类的方法
    def la():
        print("lalala...")

class LiuChan(LiuBei):
    # 子类独有成员
    weight = 180

    def douququ(self):
        print("乐不思蜀")

    def drink(self):
        print("小口吃饭 小口喝酒")
        super().drink()

    # 重载绑定类的方法
    def la():
        print("还需要别人帮你 擦屁股")
        # 父类中的la只能通过父类去访问 父类名.方法名()
        LiuBei.la()

# 表示子类继承父类之后 并没有将父类中的成员占为己有 而是拥有访问的权利
print(LiuChan.__dict__)
print(LiuChan.sex)
LiuChan.walk(1)
# print(LiuChan.wife)

# 所有类都是object的子类
result = issubclass(type, object)
print(result)

# 第一个参数如果是第二个参数的子类 则返回True 否则返回False
result2 = issubclass(LiuChan, LiuBei)
print(result2)

# 访问子类独有的成员
LiuChan.douququ(1)
print(LiuChan.weight)

# 访问继承来的方法
LiuChan.say(1)

# 访问重载后的方法 然后再方法里面访问父类的此方法
LiuChan.la()
