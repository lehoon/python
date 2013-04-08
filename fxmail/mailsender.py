from smtplib import SMTP as smtp

class MailSender:
	__smtp         = None
	__host         = " "
	__port         = " "
	__username     = " "
	__password     = " "
	__content_type = " "

	def __init__(self, host, port, username, password):
		self.__host         = host
		self.__port         = port
		self.__username     = username
		self.__password     = password
		self.__smtp         = smtp(self.__host, self.__port)
		self.__content_type = """Content-Type: text/html; charset=\"utf-8\""""

	def __del__(self):
		self.__smtp.quit()

	def sendMail(self, frm, to, subject, msg):
		try:
			self.__smtp.ehlo()
			self.__smtp.login(self.__username, self.__password)
			_msg = ("From: %s\r\n"
							"TO:%s\r\n"
							"Subject:%s\r\n"
							"%s\r\n\r\n"
							"%s\r\n")%\
							(frm,\
								to,\
								subject,\
								self.__content_type,\
								msg)
			self.__smtp.sendmail(frm, to, _msg)
		except Exception:
			print 'Error: unable to send email'


if __name__ == "__main__":
    sender = MailSender('smtp.163.com', 25, 'lehoon', 'dddddddd')
    sender.sendMail('lehoon@163.com', 'lehoons@gmail.com', '你好', '你是谁？')