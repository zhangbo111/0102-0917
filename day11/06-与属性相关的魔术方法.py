# 与属性相关的魔术方法
class Man:
    sex = "女"
    name = '刘建鑫'
    color = "绿色"
    age = 38
    def __init__(self):
        self.hobby = "在大街上看美女"
        self.hair = 'green'
    def can(self):
        print("吊打所有python工程师")
    def say(self):
        print("我很心疼牛")
    def __getattr__(self, item):
        '''
        触发时机：当访问类和对象不存在的成员属性的时候
        功能：1、防止访问不存在的属性报错  2、可以为不存在的属性设置默认值
        :param item:访问的不存在的属性名
        :return: 可以有也可以没有
        '''
        # print(1, item, type(item))
        if item == "weight":
            return "70kg"
        elif item == "height":
            return 180
        else:
            return "你访问的成员属性不存在"

    # def __getattribute__(self, item):
    #     '''
    #     触发时机：访问对象成员的时候触发（不管存在与否） 优先触发
    #     功能：限制和过滤掉不可以被访问的成员属性
    #     :param item:访问的成员属性名
    #     :return:可以有也可以没有 （一般情况下有）
    #     '''
    #     # print(3, item)
    #     if item == "hair":
    #         # return self.hair 不能用 因为会触发递归调用__getattribute__函数
    #         # 通过object基类获取self(bqt)对象的item（hair）属性的值(green)
    #         print(1, object.__getattribute__(self, item))
    #         return object.__getattribute__(self, item)
    #     else:
    #         return "对不起 您访问的成员属性不存在或者不允许访问"

    def __setattr__(self, key, value):
        '''
        触发时机：对成员属性进行重新设置的时候（不管是否存在）
        功能：限制和过滤成员属性的修改
        :param key:成员属性名
        :param value:成员属性值
        :return: 无
        '''
        # print(7, key, value)
        if key == "name" or key == "sex":
            pass
        else:
            # 通过object基类设置self对象的属性名为key的值为value
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        '''
        触发时机：删除对象的成员属性的时候
        功能：过滤掉不可以删除的对象属性
        :param item: 删除的成员属性名称
        :return: 无
        '''
        print(8, item)
        if not (item == "age"):
            # 通过object基类删除self对象的item属性
            object.__delattr__(self, item)
# 实例化对象
bqt = Man()
# 访问c类和对象不存在的成员属性
# print(2, bqt.weight)
# print(3, bqt.height)
# print(4, bqt.length)
# 第一次访问
# print(5, bqt.hair)
# print(6, bqt.color)
bqt.name = "关公"
print(bqt.name)
bqt.cloth = "white"
print(bqt.cloth)
bqt.age = 39
print(bqt.age)

print(bqt.__dict__)
del bqt.age
del bqt.hair
print(bqt.__dict__)
