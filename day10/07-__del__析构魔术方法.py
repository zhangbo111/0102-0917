# 析构魔术方法
class Movie:
    name = "狗十三"
    times = "1.5h"
    def juqing(self):
        print("青春期的叛逆")
    def actor(self):
        print("一个十三岁的小女孩")
    def __del__(self):
        '''
        触发时机：当对象没有用的时候触发（手动删除或者全部执行完毕 回收内存）
        功能：使用完对象回收资源
        参数：至少接收self对象
        返回值：无
        '''
        print("del析构方法被触发")
# 实例化对象
gss1 = Movie()
gss2 = gss1
print(gss1, gss2)
print('=========开始============')
del gss1
del gss2
print("==========结束==========")
