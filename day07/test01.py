# def print_fun(a):
#     print("hello world 雷吼")
#     return a
name = '字母哥'

print(__name__)
# 当本脚本执行的时候 __name__ == "__main__" 才会成立
if __name__ == "__main__":
    # 把本脚本导入到别的脚本中 别的脚本不可以访问这里
    name = "裤子嘛"
    print('本脚本自己执行才会执行')

