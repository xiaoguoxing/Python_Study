# 切片
L = ['123', 'abc', 'def', '321']
# print(L[0:3])
# print(L[:3])
# print(L[-1])
# print(L[-2:])
# print(L[:])
L2 = list(range(100))
# print(L2[10:20])
# print(L2[:10:2]) 前10个每2个取一个
# print(L2[::5]) 所以数每五个取一个
L3 = ('123', 'abc', 'def', '321')
# print(L3[0:2])
L4 = '123abcdef321'
print(L4[::-1])
L5 = '1_2_3_4_5'
print(list(L5[::2]))
print([s for s in L5 if s!='_' ])
#test
def trim(s):
    if s[:1]==' ':
        return trim(s[1:])
    elif s[-1:]==' ':
        return trim(s[:-1])
    else:
        return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
