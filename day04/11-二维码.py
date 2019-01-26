# 包（模块或者叫做文件）：封装好的代码，直接调用即可
# import表示导入包的意思 qrcode表示包的名称
import qrcode
# 生成 写入二维码的内容
content = input('请输入你想说的话：')
# make表示声明二维码图片
# 制作二维码图片的同时 将content写入二维码图片
img = qrcode.make(content)
# 保存图片
img.save('1.png')
# 提示
print('您的二维码生成成功，请陛下查阅')
