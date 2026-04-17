# Iterable 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
from collections.abc import Iterable
print(isinstance([], Iterable))
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter('abc'), Iterator))
