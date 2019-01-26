str1 = """
it may be that whatever the enigmatic telephone call had required professor 
blinkwell to arrange before 5 p.m. tomorrow had been accomplished when 
Myra returned to lunch, for he met her in his usual mood of cheerful complacency. 
"""
# 练习：把第一行的it may be变为大写IT MAY BE，替换it may be
#       把第二行的blinkwell变为Blinkwell
#       把第三行进行大小写互换
result1 = str1.splitlines()
# print(result1)
# 第一行
line1 = result1[1]
result2 = line1[:9]
result3 = result2.upper()
result4 = line1.replace('it may be', result3)
# print(result4)
# 第二行
line2 = result1[2]
result5 = line2.capitalize()
print(result5)
# 第三行
line3 = result1[3]
result6 = line3.swapcase()
print(result6)



