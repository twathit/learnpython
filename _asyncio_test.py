# -*- coding: utf-8 -*-
__author__ = 'Edward'
import asyncio
import threading
@asyncio.coroutine
def hello():
    print('Hello,world %s'%threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again %s'%threading.currentThread())
loop=asyncio.get_event_loop()
task=[hello(),hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()