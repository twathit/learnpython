# -*- coding: utf-8 -*-
__author__ = 'Edward'
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr=input('From:')
password=input('password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')
msg=MIMEText('Hello,send by python','plain','utf-8')
'''
msg=MIMEText('<html><body><h1>Hello</h1>'+
             '<p>Have a seat upon this <a href="http://www.weibo.com/6205470074/profile?rightmod=1&wvr=6&mod=personinfo" target="blank">branch<a> of mine</p>'+
             '</body><html>','html','utf-8')
'''
msg['From']=_format_addr('Python 爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候，闷声发大财','utf-8').encode()
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()