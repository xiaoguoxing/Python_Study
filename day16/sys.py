import os
# 系统名称
# print(os.name)
# 环境变量
# print(os.environ.get('PATH'))

print(os.path.abspath('.'))

p = os.path.join(os.path.abspath('.'), 'testdir')

# 新建一个目录
# os.mkdir(p)
# 删除一个目录
# os.rmdir(p)

p1 = os.path.join(os.path.abspath('.'), '1.txt')
# 最后一个始终是最后一级目录名
# p2 = os.path.split(p1)
# 扩展名
# p2 = os.path.splitext(p1)
# print(p2)

# os.rename('1_2.txt', '1.txt')
# os.remove('2.txt')
# l = [x for x in os.listdir('.') if os.path.isdir(x)]
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)