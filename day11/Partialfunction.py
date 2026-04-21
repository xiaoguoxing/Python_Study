#偏函数
import functools

int('1234')
int('1234',base=2)
int('1234',2)

# def int2(x,base=2):
#     return int(x,base)

int2 = functools.partial(int,base=2)

int2('1000000')