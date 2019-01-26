# dir魔术方法
class Apple:
    color = "red"
    weidao = "甜的"
    def eat(self):
        print("要一口 变成苹果公司")
    def fall(self):
        print("从天掉下来 变成万有引力")
    def __dir__(self):
        '''
        触发时机：dir(对象)的时候
        :return:序列 （列表 集合 元组）
        '''
        # 获取self（plus8）对象可以访问的所有的成员（属性和方法）
        list1 = object.__dir__(self)
        # 过滤掉魔术方法 只留下自定义成员
        list2 = []
        for i in list1:
            if not (i.startswith("__") and i.endswith("__")):
                list2.append(i)
        return list2
plus8 = Apple()
# 获取当前对象所有的自定义成员
result = dir(plus8)
print(result)
