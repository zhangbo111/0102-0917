class Banana:
    color = "yellow"
    length = "20cm"
    def __init__(self):
        # 对象独有的成员
        self.pi = "维生素"
    def weidao(self):
        print("甜甜的")
    def func(self):
        print("润肠通便")
# 实例化对象
b1 = Banana()
print(hasattr(b1, "pi"))
print(hasattr(b1, "length"))
print(hasattr(Banana, "weidao"))
# Banana类没有huai的成员
print(hasattr(Banana, "huai"))
# 类不可访问对象的独有成员
print(hasattr(Banana, "pi"))

# 获取对象指定成员的值
print(getattr(b1, "pi"))
print(getattr(b1, "color"))
print(getattr(b1, "func"))
# 获取对象中不存在的成员 第三个参数是默认值
print(getattr(b1, "weight", "90g"))

# 给指定的对象设置指定的成员属性的值
# b1.face = '很长'
setattr(b1, "face", "很长")
print(getattr(b1, "face"))

print(b1.color)
delattr(b1, "color")
print(b1.color)
