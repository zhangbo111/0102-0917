# 制作蛋糕
class MakeCake:
    # 和面
    def huomian(self):
        print("和面操作")
    # 发酵
    def fajiao(self):
        print("发酵操作")
    # 烘烤
    def hongkao(self):
        print("烘烤操作")
    # 切形状
    def qiexingzhuang(self):
        print("切形状操作")
    # 抹奶油
    def monaiyou(self):
        print("抹奶油操作")
    # 放水果
    def fangshuiguo(self):
        print("放水果操作")
    # 打包
    def dabao(self):
        print("打包操作")
        return "完整的蛋糕"
    # 获取蛋糕的方法
    def __call__(self, who):
        print("制作者：", who)
        self.huomian()
        self.fajiao()
        self.hongkao()
        self.qiexingzhuang()
        self.monaiyou()
        self.fangshuiguo()
        result = self.dabao()
        return result
mc = MakeCake()
# 当对象当做函数的时候进行调用
r = mc("向洋大厨")
print(r)
