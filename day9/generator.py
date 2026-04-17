# 生成器：generator
g = (x for x in range(1,11))
for x in g:
    pass
    # print(x)

def fib(max1):
    n, a, b = 0, 0, 1
    while n < max1:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g1 = fib(5)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# for x in g1:
#     print(x)
# while True:
#     try:
#         print(next(g1))
#     except StopIteration as e:
#         print(e.value)
#         break
def triangles():
    curren = [1]
    while True:
        yield curren
        print(curren[1:])
        curren = [1]+[a+b for a,b in zip(curren,curren[1:])]+[1]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
