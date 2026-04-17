# # 迭代
# from collections.abc import Iterable
#
# D = {'a':1,'b':2,'c':3,'d':4,'e':5}
# for i in D.keys():
#     print(i)
# for i in D.values():
#     print(i)
# for (key,value) in D.items():
#     print(key,value)
#
# # isinstance(D,Iterable)判断是否可迭代
#
# L = ['a','b','c','d','e']
# for k,v in enumerate(L):
#     print(k,v)
#
# L2 = [(1,2),(3,4),(5,6),(7,8)]
# for k,v in L2:
#     print(k,v)


def findMinAndMax(L):
    if not L:
        return None, None
    # else:
    #     return min(L), max(L)
    min1 = L[0]
    max1 = L[0]
    for item in L:
        if item < min1:
            min1 = item
        elif item > max1:
            max1 = item
    return min1, max1

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
