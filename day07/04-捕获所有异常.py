# try:
#     print(num)
#     f = open('2.txt')
# # 捕获所有异常
# except:
#     print('捕获了异常，但是不知道是何种异常')

try:
    print(num)
    f = open('2.txt')
# 捕获所有异常 e就是异常信息描述
except Exception as e:
    # 这个可以打印出描述信息
    print("打印描述信息：", e)
