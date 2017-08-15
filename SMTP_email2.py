# -*- coding: utf-8 -*-
__author__ = 'Edward'
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
from email import encoders
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input('From:')
password=input('password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')
msg=MIMEMultipart()
msg['From']=_format_addr('Python 爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候，闷声发大财','utf-8').encode()
m=MIMEMultipart('alternative')
msg.attach(m)
m.attach(MIMEText('Send with file','plain','utf-8'))
m.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p><img src="cid:0"></p></body></html>','html','utf-8'))
with open(r'd:\1.jpg','rb') as f:
    mime=MIMEBase('image','jpeg',filename='me.jpg')
    mime.add_header('Content-Disposition','attachment',filename='me.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()