"""
python 抽取数据库记录发送邮件

"""
import MySQLdb
import os, smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.message import Message
from email.header  import Header

MAIL_HOST = "smtp.163.com"
MAIL_USER = "lehoon"
MAIL_PASS = "dddddddddd"
MAIL_POSTFIX = "163.com"
MAIL_FROM = MAIL_USER + "<"+MAIL_USER + "@" + MAIL_POSTFIX + ">"

"""
	发送邮件
"""
def send_mail(recvmail, subject, content, filename = None):
    try:
        message            = MIMEText(content,'html',_charset='UTF-8') #设置UTF-8编码
        message["Subject"] = Header(subject, 'utf-8')
        message["From"]    = MAIL_FROM
        message["To"]      = recvmail

        smtp = smtplib.SMTP()
        smtp.connect(MAIL_HOST)
        smtp.login(MAIL_USER, MAIL_PASS)
        smtp.sendmail(MAIL_FROM, recvmail, message.as_string())
        smtp.quit()
        return True
    except Exception, errmsg:
        print "Send mail failed to: %s" % errmsg
        return False

"""
获取数据库连接
"""
def    getconn(hostname, username, password):
	conn   = MySQLdb.connect(host=hostname, user=username, passwd=password)
	return conn

"""
关闭数据库连接
"""
def    closeconn(conn):
	with conn:
		conn.close


"""
具体抽取数据库邮件列表，法搜邮件
"""
def   dosendmail(conn):
	cursor = conn.cursor()

	conn.select_db('fxshop')
	count  = cursor.execute('select * from sys_mailbox ')
	print 'total:', count

	numberrows = int(cursor.rowcount)

	for i in range(numberrows):
		row = cursor.fetchone()
		print row[0], row[1], row[2], row[3], row[4]
		send_mail(row[1], row[2], row[3])



if __name__ == "__main__":
	conn = getconn("42.121.129.188", "mysql", "hope2013")
	dosendmail(conn)
	closeconn(conn)

