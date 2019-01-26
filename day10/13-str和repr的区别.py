# 将一个语句转换为字符串之后 在按python语句进行执行
# str是可以实现的 但是repr是不可以实现的
val = "1+1"
result1 = eval(str(val))
print(result1)
result2 = eval(repr(val))
print(result2)
