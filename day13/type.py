import types

print(type('123'))
print(type(123))


def dog(name):
    pass


print(type(dog) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type((x for x in range(1, 10))) == types.GeneratorType)

isinstance([1, 2, 3, 4], (list, tuple))
isinstance((1, 2, 3, 4), (list, tuple))
isinstance({'a': 1}, dict)
isinstance(1, int)
isinstance('1', str)

dir('123')


# getattr()、setattr()以及hasattr()

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(
    hasattr(obj, 'x'),
    hasattr(obj, 'power'),
    getattr(obj, 'x'))

setattr(obj, 'x', 10)

print(getattr(obj, 'x'))
# print(getattr(obj, 'z')) # 报错
print(getattr(obj, 'z',20))