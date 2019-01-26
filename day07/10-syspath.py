import sys
'''
import test01 （模块名）
寻找模块名第一时间会去sys.path里面寻找，且按照顺序查找
而且第一个路径是当前路径
'''
print(sys.path)

import os
# 因为os是一个单独的模块名 脚本不可以使用os命名
result = os.print_fun(1)
print(result)
