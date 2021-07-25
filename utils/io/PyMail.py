# *_*coding:utf-8 *_*
"""
Author：szj
Descri：
"""
import poplib
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import logging

logger = logging.getLogger(__name__)


class SimpleEmail:
    def __init__(self, host=None, port=None, user=None, passwd=None, sender=None):
        """邮件配置

        :param host:
        :param port:
        :param user:
        :param passwd:
        :param sender: 发件人名称，最好取一个好听的名字
        """
        self.host = host or "smtpdm.aliyun.com"
        self.port = int(port) if port else 80
        self.user = user or "elkmonitor@kaisasecurities.site"
        self.pass_ = passwd or "Sz0a3ncf2c2ZFbLj"

        # 发件人的别名
        self.sender = sender or "做好事不留名"

    def loging_POP3(self):
        try:
            server = poplib.POP3(self.host, self.port)
            server.user(self.user)
            server.pass_(self.pass_)
            return server
        except Exception as why:
            raise Exception("邮箱连接错误")

    def loging_POP3_SSL(self):
        try:
            server = poplib.POP3_SSL(self.host, self.port)
            server.user(self.user)
            server.pass_(self.pass_)
            return server
        except Exception as why:
            raise Exception("邮箱连接错误")

    def loging_IMAP4(self):
        try:
            server = imaplib.IMAP4(host=self.host, port=self.port)
            server.login(self.user, self.pass_)
            result = server.select("INBOX")
            return server
        except Exception as why:
            raise Exception("邮箱连接错误")

    def loging_IMAP4_SSL(self):
        try:
            server = imaplib.IMAP4_SSL(host=self.host, port=self.port)
            server.login(self.user, self.pass_)
            result = server.select("INBOX")
            return server
        except Exception as why:
            raise Exception(f"邮箱连接错误{why}")


class Mailer(SimpleEmail):
    def send(
        self,
        title=None,
        body=None,
        strType="html",
        attachment=[],
        imgs: dict = {},
        to=[],
        cc=[],
    ):
        """发送邮件

        :param title: 主题
        :param body: 正文 ，非必须
        :param strType: 邮件内容的格式
        :param attachment: 附件路径 ，非必须
        :param imgs: 邮件正文的图片路径及对应的标签名称 ，非必须
        :param sender: 发件人
        :param to: 收件人
        :param cc: 抄送人
        :return:
        """

        message = MIMEMultipart()  # 添加对象

        # 发送附件
        if attachment:
            for fpath in attachment:
                try:
                    fname = fpath.split("\\")[-1]
                    apart = MIMEApplication(open(fpath, "rb").read())
                    apart.add_header(
                        "Content-Disposition", "attachment", filename=f"{fname}"
                    )
                    message.attach(apart)
                except Exception as why:
                    logger.error(f"加载附件报错:{why}")

        # 发送文本对象
        if strType == "plain":
            strApart = MIMEText(body, "plain", "utf-8")
        else:
            strApart = MIMEText(body, "html", "utf-8")

        # 邮件正文插入图片
        if imgs:
            for imgpath, name in imgs.items():
                f = open(imgpath, "rb")
                msgImage = MIMEImage(f.read())
                f.close()
                msgImage.add_header("Content-ID", name)
                message.attach(msgImage)

        if strApart:
            message.attach(strApart)
        if cc:
            message["Cc"] = ";".join(list(set(cc)))
        if to:
            message["To"] = ";".join(list(set(to)))  # 邮件上显示的收件人,如果是多人,需要将 list转 string
        message["Subject"] = Header(title, "utf-8")  # 邮件主题
        message["From"] = self.sender  # getattr(cls(), "sender")  # 邮件上显示的发件人

        try:
            smtp = smtplib.SMTP()  # 创建一个连接
            smtp.connect(self.host)  # 连接发送邮件的服务器
            smtp.login(self.user, self.pass_)  # 登录服务器
            smtp.sendmail(self.user, to + cc, message.as_string())  # 填入邮件的相关信息并发送
            logger.info("恭喜你，邮件发送成功！")
            smtp.quit()
        except Exception as why:
            logger.error(f"邮件发送失败：\n{why}")


if __name__ == "__main__":
    RECEIVERS = ["songzhij@kaisagroup.com"]  # 接收邮箱
    CC = []

    # 邮件标题
    TITLE = "hello songzhijhun"

    # 邮件正文
    BODY = """
<html>
    <!-- 网页的标题、图标... -->
    <head>
        <mate charset="utf-8">
        <title>Process_Monitor</title>
    </head>
    <!-- 网页的具体内容 -->
    <body>

        <img src="cid:avatar" width="900" height="700" />
        <img src="cid:avatar" width="900" height="700" />

    </body>
</html>"""

    # 附件地址
    ATTATCHMENT = []
    IMAGES = {
        "/Users/a12345/PycharmProjects/kaisa_projects/news_sentiment_decision/avatar.jpg": "avatar"
    }
    mailer = Mailer(sender="jkljkl")
    mailer.send(
        title=TITLE, body=BODY, attachment=ATTATCHMENT, imgs=IMAGES, to=RECEIVERS
    )
