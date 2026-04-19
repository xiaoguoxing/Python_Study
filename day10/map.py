# def f(x):
#     return x*x
#
# L = map(f,[1,2,3,4,5])
#
# print(list(L))
#
# L2 = map(str,[1,2,3,4,5])
#
# print(list(L2))
#
# from functools import reduce
# def f2(x,y):
#     return x+y
# L3 = reduce(f2,[1,2,3,4,5])
#
# print(L3)
# L4 = {'0':0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
# def fn3(s):
#     def f(x,y):
#         return x*10+y
#     def g(x):
#         return L4[x]
#     # return reduce(f,map(g,s))
#     return reduce(lambda x, y: x * 10 + y,map(g,s))
#
# print(fn3('13579'))

def normalize(name):
    return f'{name.upper()[:1]}{name.lower()[1:]}'

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):
    return reduce(lambda x, y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    if '.' in s:
        a,b=s.split('.')
    else:
        a,b=s,''
    num={str(i):i for i in range(10)}
    a_float=reduce(lambda x,y:x*10+y,map(lambda str:num[str],a))
    b_float=reduce(lambda x,y:x*10+y,map(lambda str:num[str],b),0)/(10**len(b))
    return a_float+b_float

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



