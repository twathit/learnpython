# -*- coding: utf-8 -*-
__author__ = 'Edward'
import threading
balance=0
lock=threading.Lock()
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(i)
        finally:
            lock.release()
t1=threading.Thread(target=run_thread(5))#,args=(5,))
t2=threading.Thread(target=run_thread(8))#,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)