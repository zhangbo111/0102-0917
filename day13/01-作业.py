a = '123'
b = '123'
# a和b的内存地址是一样的
print(id(a))
print(id(b))
# 同一个地址引用的变量名不一样
# 变量名 == 变量名 其本质就是判断变量名对应的值是否相等
print(a == b)
# is的意思当is左边两边的变量名指定的值所在的地址是一样的时候才为True
# 否则为False
print(a is b)

def bar(multiple):
    # multiple =2
    def foo(n):
        # n = 3
        return multiple ** n
    return foo

print(bar(2)(3))

a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1
print(a)
