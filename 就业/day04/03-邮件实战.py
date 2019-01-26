import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class Send_Email(object):

    def __init__(self, num):
        self.num = num
        # print(self.num)
        self.smtp = self.produce_smtp()
        # print(self.smtp, type(self.smtp))
        # 发送邮件
        self.send_email()

    # 登录邮箱操作
    def produce_smtp(self):
        # 创建一个邮件对象
        smtpObj = smtplib.SMTP()

        # 连接邮件服务器
        smtpObj.connect("smtp.163.com")

        # 登录邮箱操作
        smtpObj.login("18679030315@163.com", "zb18679030315")

        return smtpObj

    # 发送邮件
    def send_email(self):
        # 定义发送邮件三要素
        sender = "18679030315@163.com"
        receiver = "376100870@qq.com"
        msg = self.get_msg(sender, receiver)
        # 发送邮件
        self.smtp.sendmail(sender, receiver, msg.as_string())
        print("发送邮件成功")

    # 获取发送邮件的实体
    def get_msg(self, sender, receiver):
        # 定义邮件的发送主题
        subject = "这是一封项目监控的邮件 请重视"
        # print(sender, receiver)
        msg = self.get_msg_content()
        # 定义信息三要素
        msg['From'] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        return msg

    # 获取指定格式的邮件内容
    def get_msg_content(self):
        if self.num == 1:
            content = "程序员的苦逼Bug生涯 要开始了"
            # 创建文本格式的邮件体
            msg = MIMEText(content, "plain", "utf-8")
            return msg
        elif self.num == 2:
            content = "<html><h1>这是一封html的邮件</h1></html>"
            msg = MIMEText(content, "html", "utf-8")
            return msg
        elif self.num == 3:
            # 获取带有内嵌图片格式的html格式体
            msg = self.get_pic()
            return msg

    # 获取图片
    def get_pic(self):

        content = "<b>some<i>HTML</i>text</b>and an image.<br><img src='cid:image1'></br>good!"
        # 有内嵌资源的时候必须定义
        # 使用related创建一个带有内嵌资源的邮件体
        msgRoot = MIMEMultipart("related")
        # 创建一个带有html的邮件体
        msgText = MIMEText(content, "html", "utf-8")
        # 将msgText和msgRoot进行关联
        msgRoot.attach(msgText)

        # 读取文件内容
        with open('1.png', "rb") as f:
            result = f.read()
        # 创建一个图片的对象
        msgImage = MIMEImage(result)
        # 指定文件的Content-ID 为image1
        msgImage.add_header("Content-ID", "image1")
        # 关联图片信息到msgRoot
        msgRoot.attach(msgImage)
        # 返回带有内嵌图片资源的对象
        return msgRoot


if __name__ == "__main__":
    '''
    1、文字形式的邮件
    2、html形式的邮件
    3、带有图片的html格式的邮件
    '''
    num = int(input("请输入要发送的邮件格式（1.文字 2.html 3.图片）："))
    Send_Email(num)
