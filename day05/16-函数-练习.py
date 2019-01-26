# 练习：声明一个hobby函数，传入“谋笑” 返回“看美女”“足球”
# 传入建鑫 返回 “看人妖” “篮球”
# 传入向洋 返回  "看星星"  ”数太阳“
# 传入 豪斌 和 昌镐  返回 “小说” “晒太阳”
# 默认值参数 如果给了name2实参 则用传递过来的实参 否则用默认的-
def hobby(name1, name2='-'):
    # print(name1, name2)
    if name1 == "谋笑":
        return "看美女", "足球"
    elif name1 == "建鑫":
        return "看人妖", "篮球"
    elif name1 == "向洋":
        return '看星星', '数太阳'
    elif name1 == "豪斌" and name2 == "昌镐":
        return "小说", "晒太阳"
mx_hobby = hobby('谋笑')
jx_hobby = hobby('建鑫')
xy_hobby = hobby('向洋')
hb_cg_hobby = hobby('豪斌', '昌镐')
print("谋笑的爱好：", mx_hobby)
print("建鑫的爱好：", jx_hobby)
print("向洋的爱好：", xy_hobby)
print("豪斌和昌镐的爱好：", hb_cg_hobby)










