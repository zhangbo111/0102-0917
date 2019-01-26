import test02
# 可以通过 模块名.变量名（函数名） 访问模块里面的信息
print(test02.name)
print(test02.age)
print(test02.hello.__name__)

from test02 import hello
# 可以通过模块直接导入指定的函数
# 直接使用函数名即可 不用通过 模块名.函数名进行访问
# 在我们只需要函数名hello 不需要使用其他的变量名或函数名
result = hello('今天吃饭了吗')
print(result)

from test02 import *
# 把所有的变量名和函数导入进来
# 也是直接使用 不需要通过模块名.变量名（函数名）来使用
print(name)
print(age)
hello('莎娃迪卡')

from test02 import name, age
# 只需要使用其中的几个变量 使用这种方式导入
print(name)
print(age)
# 没有导入hello函数 则不可以使用
hello('1')
