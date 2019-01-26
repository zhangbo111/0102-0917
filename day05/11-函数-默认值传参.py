# shouchi这个参数有默认的值
# 注意：默认值参数 写在正常参数之后
def wuxia(jianghu, shouchi='青龙偃月刀'):
    print("jianghu:", jianghu)
    print("shouchi:", shouchi)
# 参数全部传递
# 如果给shouchi进行传参 则使用传过去的参数
wuxia('笑傲江湖', '紫青宝剑')
# 如果没有给shouchi传参 则shouchi使用的是默认值参数
wuxia('神雕侠侣')







