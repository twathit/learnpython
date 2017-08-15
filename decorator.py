import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begin call %s()" % (text, func.__name__))
            func(*args, **kw)
            print("%s end call %s()" % (text, func.__name__))
            #return ret
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        #f = text
        #text = ''
        return decorator(text)
@log('execute')
def f():
    print('12')