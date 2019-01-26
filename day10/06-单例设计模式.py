# 单例设计模式 可以节约空间
class GuangZhou:
    # 类的成员属性
    cloud = "white"
    tree = "green"
    # 声明一个对象用于存储当前类的对象
    obj = None
    # 创建对象的魔术方法
    def __new__(cls, *args, **kwargs):
        print(1, cls.obj)
        # 如果是第一次要求创建对象则cls。obj=None
        if cls.obj == None:
            cls.obj = object.__new__(cls)
            print(2, cls.obj)
            # 返回创建的对象(第一次)
            return cls.obj
        # 不是第一次的情况
        else:
            # 直接返回第一次创建的对象（第二次来的时候）
            return cls.obj
# 实例化对象
gz1 = GuangZhou()
print(3, gz1)
# 第二次返回的是第一次创建的对象
gz2 = GuangZhou()
print(4, gz2)
# 第三次返回的是第一次创建的对象
gz3 = GuangZhou()
print(5, gz3)
