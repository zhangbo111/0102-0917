class Car:
    # 属性
    color = "red"
    _price = 100
    def zaiRen(self):
        print(self._price)
        print("主人 你想去哪里")
print(Car.color)
# 类外不可以访问
# print(Car.price)
# 通过对象调用方法 在类中对受保护的属性进行访问
benci = Car()
benci.zaiRen()
# 查看Car的属性 受保护的成员名字没有变更
print(Car.__dict__)
# 如果非要在类外进行访问 可以使用如下方式  不推荐
print(Car._price)
