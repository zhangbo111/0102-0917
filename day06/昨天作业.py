def jiami(phone):
    print("需要加密的电话：", phone)
    # 声明一个新的字符串  用于接收加密后的数据
    newStr = ''
    for i in phone:
        newStr += str(int(i) * 7 % 10)
    return newStr

result1 = jiami("18679030315")
print("加密之后的内容：",result1)

def jiemi(data):
    # 声明一个字符串 用于接收解密后的电话
    phone = ''
    for i in data:
        if int(i):
            phone += str(10 - int(i) * 7 % 10)
        else:
            phone += str(0)
    return phone

phone = jiemi(result1)
print('解密之后的电话：', phone)





