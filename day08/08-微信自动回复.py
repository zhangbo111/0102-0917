import itchat
from itchat.content import *
import time
# 监听微信消息 TEXT表示监听的是文本消息
@itchat.msg_register([TEXT, PICTURE])
def text_reply(msg):
    # print(msg)
    msg_text = msg['Text']
    print(msg_text, type(msg_text))
    if "年" in msg_text:
        # 获取对象的name
        from_user = msg['FromUserName']
        # 获取到省市备注名
        user = msg['User']
        print(user)
        province = user.get('Province')
        city = user.get('City')
        name = user.get('RemarkName')
        # 如果获取不到备注名 则获取昵称
        if not name:
            name = user.get('NickName')
        print(province, city, name)
        # 如果都能获取到省市和name的情况下 制作返回信息
        if all([province, city, name]):
            return_msg = "来自{}省{}市的{}，happy newyear".format(province,city,name)
        else:
            return_msg = "{}, 恭喜发财 来年行大运".format(name)

        time.sleep(2)
        # 给对方回复消息
        itchat.send(return_msg, from_user)
if __name__ == "__main__":
    # 登录操作 hotReload=True 热重载 表示下次不用再次登录
    itchat.auto_login(hotReload=True)
    # 保持程序不退出 一直处于运行状态
    itchat.run()
