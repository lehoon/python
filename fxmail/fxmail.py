﻿#!/usr/bin/env python
import os, smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
MAIL_LIST = ["cores@126.com"]
MAIL_HOST = "smtp.163.com"
MAIL_USER = "lehoon"
MAIL_PASS = "dddddddddddd"
MAIL_POSTFIX = "163.com"
MAIL_FROM = MAIL_USER + "<"+MAIL_USER + "@" + MAIL_POSTFIX + ">"
def send_mail(subject, content, filename = None):
    try:
        message = MIMEMultipart()
        message.attach(MIMEText(content))
        message["Subject"] = subject
        message["From"] = MAIL_FROM
        message["To"] = ";".join(MAIL_LIST)
        if filename != None and os.path.exists(filename):
            ctype, encoding = mimetypes.guess_type(filename)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/", 1)
            attachment = MIMEImage((lambda f: (f.read(), f.close()))(open(filename, "rb"))[0], _subtype = subtype)
            attachment.add_header("Content-Disposition", "attachment", filename = filename)
            message.attach(attachment)
        smtp = smtplib.SMTP()
        smtp.connect(MAIL_HOST)
        smtp.login(MAIL_USER, MAIL_PASS)
        smtp.sendmail(MAIL_FROM, MAIL_LIST, message.as_string())
        smtp.quit()
        return True
    except Exception, errmsg:
        print "Send mail failed to: %s" % errmsg
        return False
if __name__ == "__main__":
    if send_mail("测试信", "我的博客欢迎您：http://flykite.blog.51cto.com/", r"F:\download\arm\releasenote.txt"):
        print "发送成功！"
    else:
        print "发送失败！"