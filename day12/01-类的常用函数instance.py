# isinstance

class Apple:
    pass
hfs = Apple()
# 检测一个对象是否是指定类的对象
print(isinstance(hfs, Apple))

a = 10
print(isinstance(a, int))
print(isinstance(a, float))
print(isinstance(a, Apple))
# 检测a是否是Apple或者int类的对象 满足一个即可
print(isinstance(a, (Apple, int)))


