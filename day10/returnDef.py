def res_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax
    return sum
s = res_sum(1,2,3,4,5,6)
s2 = res_sum(1,2,3,4,5,6)
# print(s==s2) #False
# print(s()==s2())

def count():
    # def a(j):
    #     return lambda :j*j
    c = lambda j:lambda :j*j
    fs = []
    for i in range(1,4):
        fs.append(c(i))
    return fs
c1,c2,c3 = count()
# print(c1())
# print(c2())
# print(c3())

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
# print(f()) # 1
# print(f()) # 1

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
