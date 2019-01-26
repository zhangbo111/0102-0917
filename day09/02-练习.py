'''
声明一个人类
属性：性别，年龄，肤色，婚否
方法：吃饭，睡觉，思考，呼吸

在方法里面随便打印些东西
实例化张飞对象这些是实例化对象特有的属性：添加属性一张嘴，两个耳朵，姓名
实例化科比对象：添加一个他特有的功能 打篮球
'''
# 声明一个人类
class Human:
    # 属性
    sex = '男'
    age = 18
    skin = "black"
    marry = "否"

    # 方法
    def eat_rice(self):
        print('每天都要吃饭 真烦人')
    def sleep(self):
        print("早睡早起 有利于新晨代谢")
    def think(self):
        print("找工作 赚大钱 迎娶白富美")
    def breath(self):
        print("最怕空气突然安静 连我的呼吸都可以听到")

# zhangFei = Human()
# kobe = Human()
#
# zhangFei.name = "张飞"
# zhangFei.mouth = 1
# zhangFei.ear = 2
# print(zhangFei.__dict__)
#
# kobe.basketball = lambda :print("永不放弃 哪怕三仰化二铁")
# print(kobe.__dict__)
# kobe.basketball()

# 打印类的值 就是他自己
print(Human)
# 打印类的类型
print(type(Human))
dulante = Human()
print(type(dulante))
# 检测类的成员
print(Human.__dict__)
# 检测对象的成员
print(dulante.__dict__)
