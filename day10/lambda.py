# 匿名函数
fn = lambda x: x * x
L = list(map(fn, range(1, 10)))
print(L)


def is_odd(n):
    return n % 2 == 1


L1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L1)
