# 两个字符串必须长度相同 且一一对应
intab = 'abcdew'
outtab = '12ej66'
# 表示生成两个字符串一一对应的关系表（绑定的过程）
str_trantab = str.maketrans(intab, outtab)

# test_str表示需要翻译的字符串
test_str = 'hello world'
# str_trantab表示翻译的对应关系
result = test_str.translate(str_trantab)
print(result)
