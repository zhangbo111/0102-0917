# 使用class声明一个类 要括号也可以不要也可以
class GirlFriend:
    # 属性
    sex = '女'
    age = 36
    name = "翠花"
    height = 165
    weight = None
    threeWei = ('36E', '2.1', '108CM')

    # 方法
    def guang(self):
        print(self)
        print('逛街真开心')

    def eat(self):
        print('吃饭时间到了')

    def cry(self):
        print('两个字，感动')

# 类的操作

# # 访问
# # 访问类的属性 类名.属性名
# print(GirlFriend.sex)
# # 访问类的方法（函数） 类名.方法名（） 有参数则传参数
# GirlFriend.cry(1)

# # 修改
# # 修改属性
# GirlFriend.name = '布莱尼'
# print(GirlFriend.name)
# # 修改方法 只能修改方法中内容 使用lambda函数
# GirlFriend.cry = lambda : print("电影真好看")
# GirlFriend.cry()

# # 删除
# # 打印出所有的成员属性和成员方法
# print(GirlFriend.__dict__)
# # 删除属性
# del GirlFriend.threeWei
# print(GirlFriend.__dict__)
# # 删除方法
# del GirlFriend.cry
# print(GirlFriend.__dict__)

# 添加
# 添加属性
# GirlFriend.hair = 'black'
# print(GirlFriend.__dict__)
# # 添加方法
# GirlFriend.see_moive = lambda :print('午夜凶铃一点都不恐怖')
# print(GirlFriend.__dict__)
# GirlFriend.see_moive()

# 对象的基本操作

# 实例化对象  类名（）
# 相当于产生一个实例 这个实例可以访问类当中的属性和方法
lingling = GirlFriend()
print(lingling.sex)
# 检测对象中的属性和方法
# lingling这个对象有访问的权利 没有占有的权利
print(lingling.__dict__)

# 访问
# 通过实例化对象.属性名 访问属性
print(lingling.height)
# 通过实例化对象.方法名() 访问方法
# 把lingling这个对象传给self
lingling.guang()

# 修改属性
print(lingling.age)
# 这个age只属于当前对象自己
lingling.age = 18
print(lingling.age)
print(lingling.__dict__)
# 修改方法 这个方法也是只属于当前对象的
lingling.eat = lambda :print('吃得太胖了 没有敢娶')
print(lingling.__dict__)
lingling.eat()

# 添加操作 只属于当前对象
lingling.skin = "yellow"
print(lingling.skin)
print(lingling.__dict__)
# 具体到每一个个体 类的对象会有一些个体化差异
# luXiaoYu = GirlFriend()
# print(luXiaoYu.skin)
# print(GirlFriend.skin)
# 添加方法名
lingling.run = lambda :print("跑步对身体好 要坚持住")
lingling.run()
print(lingling.__dict__)

# 删除特有的属性和方法
del lingling.skin  # 删除属性
del lingling.run  # 删除方法
print(lingling.__dict__)

# 删除类里面的方法和属性是不可以的
# del lingling.name
# del lingling.eat
# print(lingling.name)
# lingling.eat()



