# -*- coding: utf-8 -*-
__author__ = 'Edward'
import re
def re_emails(str):
    re_email1=re.compile(r'([A-Za-z\.]+)@(\w+)\.com')
    return re_email1.match(str).groups()
def re_emailc(str):
    re_email2=re.compile(r'<*([A-Za-z\s]*)>*([\w\.]*)@(\w+)\.([comorg])')
    return re_email2.match(str).groups()
print(re_emailc('<Tom Paris>tom@voyagar.org'))
print(re_emailc('bill.gates@microsoft.com'))
