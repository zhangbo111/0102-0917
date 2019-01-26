# 模块单例模式
class My_Singleton(object):
    def foo(self):
        print('单例模式')


my_singleton = My_Singleton()
if __name__ == "__main__":
    print(my_singleton)
