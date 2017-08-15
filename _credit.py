# -*- coding: utf-8 -*-
__author__ = 'Edward'
import hashlib
db={}
def calc_md5(str):
    md5=hashlib.md5()
    md5.update(str.encode('utf-8'))

    return md5.hexdigest()
def register(user,password):
    db[user] = calc_md5(password+user+'the salt')
    #return db[user]
'''
db = {
    'michael': 'ab281e4aedd3e9981074f8f4c380eb3e',1
    'bob': '2071ea452154a0d74bc3c77f032ff27a',
    'alice': 'b430935d83cbe1e08e46fa2235164a98'
}
'''
def login(user, password):
    #r=register(user,password)
    r=calc_md5(password+user+'the salt')
    if db[user]==r:
        print('Pass')
    else:
        print('Try again!')
'''
login('michael', '123456')
login('bob','abc999')
login('alice','alice2008')

#calc_md5('michael', '123456')
'''
while True:
    x=int(input('Register,print 1\nLogin in, print 2\nQuit,print 0\n'))
    if x==0:
        break
    elif x==1:
        user=input('Set your username:')
        password=input('Set your password:')
        register(user,password)
        login(user,password)
    elif x==2:
        user = input('Print your username:')
        password = input('Print your password:')
        login(user, password)
    else:
        print('Wrong number!')
