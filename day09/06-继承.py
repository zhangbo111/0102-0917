class Fruit:
    water = "水甜"
    def vitamen(self):
        print("补充维他命")
# Apple继承了父类Fruit的所有成员
# 在子类的名称后面的括号内写上父类的名称
class Apple(Fruit):
    '''
    Apple是子类可以使用父类中的成员属性和成员方法
    Fruit是Apple的父类
    '''
    color = 'red'
    # 重载父类中的方法
    def vitamen(self):
        # 可以使用super来访问重载之后的父类中的方法
        super().vitamen()
        print("维他命虽好 可不要吃多了 以免吸收不了")
# 如果访问的成员子类里面没有 则访问父类中的成员
print(Apple.water)
# 实例化Apple的对象
hongfushi = Apple()
# 访问vitamen方法 1、访问对象的方法 2、访问子类中的方法 3、访问父类里面的方法
# 前面查找到了 后面就不需要查找
hongfushi.vitamen()
# super要用对象去调用 不能用类
# Apple.vitamen(1)

