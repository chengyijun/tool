# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: t1.py
@time: 2021/6/3 10:11
@desc:
"""
# import smtplib #发送邮件
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    """
    请记得先填写授权码再使用哦
    """
    host = 'smtp.qq.com'  # 邮箱的接口
    port = '25'  # 端口
    pwd = ''  # 授权码

    def __init__(self, sender: str, receiver: str, subject: str, content: str, file: str) -> None:
        self.sender = sender  # 发送方
        self.receiver = receiver  # 接收方
        self.subject = subject  # 邮件主题
        self.content = content  # 邮件正文
        self.file = file  # 附件文件

    def create_email(self) -> str:
        """
        创建邮件
        :return:
        """
        msg = MIMEMultipart('mixed')
        # 标题
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.receiver
        # 设置正文
        text = self.content
        text_plain = MIMEText(text, 'plain', 'utf-8')  # 正文转码
        msg.attach(text_plain)
        # 设置附件
        with open(self.file, 'rb') as f:
            SendImageFile = f.read()
        image = MIMEImage(SendImageFile)
        image['Content-Disposition'] = 'attachment;filename="attach.jpg"'
        msg.attach(image)
        return msg.as_string()

    def send(self):
        try:
            smtp = smtplib.SMTP_SSL(self.host, self.port)  # 创建一个邮件服务
            # smtp.connect(host)
            smtp.login(self.sender, self.pwd)
            email = self.create_email()
            smtp.sendmail(self.sender, self.receiver, email)
            time.sleep(3)
            smtp.quit()  # 退出邮件服务
        except Exception as e:
            print(e)
        print("邮件发送成功！")


def main():
    SendEmail('cyjmmy@qq.com', 'cyjmmy@qq.com', 'joke', 'for tank', './kkx.jpg').send()


if __name__ == '__main__':
    main()
