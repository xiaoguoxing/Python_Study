## 函数的参数
# 位置参数
def init1(x):
    return x * x


print(init1(5))


# 默认参数------------------------
def init2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(init2(5, 5))


def init(isFirst=True):
    print(isFirst)


init(False)


def school(name, age=6, gender='F', city='BeiJing'):
    print(name)
    print(age)
    print(gender)
    print(city)


print(school('wu', gender='M'))


def addL(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(addL())


# print(addL())
# print(addL())
# 可变参数------------------------
def calc(*nums):
    sum = 0
    for num in nums:
        sum = sum + num * num
    return sum


# print(calc(1, 2, 3))
print(calc(*[1, 2, 3]))


# 关键字参数------------------------
def person(name, **kwargs):
    print(name)
    print(kwargs)


extra = {'abc': 'cba', 'abcd': 'dcba'}
# person('zhangsan',abc='abc',abcd='dcba')
# person('zhangsan',abc=extra['abc'])
person('zhangsan', **extra)


# 命名关键字参数
def person2(name, *args,city:str='shenzhen',age:int):

    print(args)
    print(name)
    print(city)
    print(age)

# person2('lisi',city='beijing',abc='qwer',zipcode=123456)
# person2('liso',*[1,2,3,4],city='Beijing',age=14)
# person2(*['lisi',2,3,4],city='Beijing',age=14)
# person2('lisi','123','321',age=5,city='Beijing',)
person2('lisi','123',age=5)
