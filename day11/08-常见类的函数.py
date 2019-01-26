class Father:
    pass
class Mother:
    pass
class Laowang:
    pass
class Son(Father, Mother):
    pass
# 检测一个类是否是另外一个类的子类 如果是返回True 否 False
result1 = issubclass(Son, Father)
result2 = issubclass(Son, Mother)
result3 = issubclass(Son, Laowang)
# 检测Son类是否是Mother类或者Laowang类的子类 满足一个就可以
result4 = issubclass(Son, (Mother, Laowang))
print(result1, result2, result3, result4)
