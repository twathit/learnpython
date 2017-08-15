# -*- coding: utf-8 -*-
__author__ = 'Edward'
import socket,time
import threading
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Welcom!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        #sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
        sock.send(b'Hello,%s!'%data)
    sock.close()
    print('Connection from %s:%s closed'%addr)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9997))
s.listen(5)
print('Waiting for connection...')
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


