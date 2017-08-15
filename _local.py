# -*- coding: utf-8 -*-
__author__ = 'Edward'
import threading
local_school=threading.local()
def process_student():
    std=local_school.name
    print('Hello, %s (in %s)' %(std,threading.current_thread().name))
def process_thread(name):
    local_school.name=name
    process_student()
t1=threading.Thread(target=process_thread('Alice'),name='Thread-A')
t2=threading.Thread(target=process_thread('Bob'),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
