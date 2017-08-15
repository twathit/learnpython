# -*- coding: utf-8 -*-
__author__ = 'Edward'
#import  threading,time
import time,threading
from threading import Thread
def loop():
    print('Thread %s is running...' %threading.current_thread().name)
    #n=0
    #while n<5:
    for n in range(5):
        #n=n+1
        print('Thread %s >>> %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('Thread %s ended' %threading.current_thread().name)
print('Thread %s is running...' %threading.current_thread().name)
#t=threading.Thread(target=loop,name='Loopthread')
t=Thread(target=loop,name='Loopthread')
t.start()
t.join()
print('Thread %s ended' %threading.current_thread().name)