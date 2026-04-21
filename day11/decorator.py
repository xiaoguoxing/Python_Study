import datetime
import functools


def log(text=None):
    if callable(text):
        func = text

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            print('begin call')
            result = func(*args, **kwargs)
            print('end call')
            return result

        return wrap
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrap(*args, **kwargs):
                print(f'{text} begin call')
                result = func(*args, **kwargs)
                print(f'{text} end call')
                return result

            return wrap

        return decorator


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            print(f'{text} {func.__name__}():')
            return func(*args, **kwargs)

        return wrap

    return decorator


@log
def now():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


now()
import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        msg = f'{fn.__name__} time: {(end - start) * 1000} ms'
        print(msg)
        return result

    return wrap


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
