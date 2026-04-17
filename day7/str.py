# 整数、浮点数、字符串、布尔值
print('个人绩效')
print('安全生产建议')
print('项目管理系统')
# name = input()
# print('input:',name)
print('1024*768 =',1024*768)
print(r'1111/ddd1\t"1111222333"')
print('''
line1
line2
line3
''')
print(r'''hello,\n world''')
num1 = 1
num2 = 1.255
bool1 = True
bool2 = False
bool3 = 1>2
# and=& or=|| not=!
print(bool3)
age = 18
if age > 19:
    print('>19了')
else:
    print('<19了')

print('hello,%s,%s' % ('world','111111'))
print('h{0}llo,w{1}rld'.format('111','222'))
a = 72
b = 83
print(f'这是：{a},这是：{b}，这是增长率：{(b-a)/a:.1%}')
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))