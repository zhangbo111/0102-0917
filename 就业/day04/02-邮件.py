# 导入邮件包
import smtplib

# 1、创建邮件对象
smtpObj = smtplib.SMTP()

# 2、连接服务器
smtpObj.connect()

# 3、登录操作
smtpObj.login()

# 4、发送邮件
smtpObj.sendmail()

# 5、退出操作
smtpObj.quit()
