# 递归
import abc


def f(x):
    if x==1:
        return 1
    return x*f(x-1)

# print(f(5))

# 尾递归
def f1(x):
    return f_iter(x,1)
def f_iter(x,y):
    if x==1:
        return y
    return f_iter(x-1,x*y)


print(f1(5))

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(3, 'A', 'B', 'C')
#     hanoi(2, 'A', 'C', 'B')
#     hanoi(2, 'C', 'A', 'B')
# hanoi(2, 'C', 'A', 'B')
