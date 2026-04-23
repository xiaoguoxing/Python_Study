# 定制类
class Screen:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Screen width: {self.width}, height: {self.height}'
    __repr__ = __str__



class Screen2:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        if self.count>=10:
            raise StopIteration()
        return self.count


for i in Screen2():
    pass
    # print(i)

class Screen3:
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        return None


# print(Screen3()[4])
# print(Screen3()[1:5])

class Screen4:
    def __getattr__(self, item):
        if item == 'count':
            return 7
        if item == 'get_count':
            return lambda :17
        raise AttributeError(f'没有这个属性：{item}')
        return None
a = Screen4()

# print(a.count)
# print(a.get_count())
# print(a.abc)

class Chain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# print(Chain().abcd.efgh)

class Screen5:
    def __init__(self):
        self.name = '123'
    def __call__(self, *args, **kwargs):
        print('我是函数')
        print(args)
        print(kwargs)

b = Screen5()
b(1,2,3,abc='123')

print(callable(Screen5()))