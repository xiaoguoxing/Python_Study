# list生成式
import os
# print(list(range(0, 11)))

# L = []
# for i in range(1,11):
#     L.append(i*i)
# print(L)

# L = [x*x for x in range(1,10) if x % 2 == 0]
# print(L)
#
# L = [x+y for x in 'ABC' for y in 'XYZ']
# print(L)

# L = [c for d in os.listdir('../') if 'day' in d for c in os.listdir('../'+d) if '.py' in c and 'main' not in c]
# print(L)

# L1 = {'a':1, 'b':2, 'c':3}
# L2 = [f'{k}={v}' for k,v in L1.items()]
# print(L2)

# L = ['Hello', 'World', 'IBM', 'Apple']
# L2 = [s.lower() for s in L]
# print(L2)

# L = [x if x % 2 == 0 else -x for x in range(1,10)]
# # for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
# print(L)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
