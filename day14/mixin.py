# 多重继承
import json


class Animal(object):
    pass


def check_value(value, name):
    if not isinstance(value, int):
        raise TypeError(f'{name}:应为数字')
    if value <= 0:
        raise ValueError(f'{name}:不应该小于0')


class JsonSerializableMixIn:
    def to_json(self):
        # 把对象的属性转换成 JSON 字符串
        return json.dumps(self.__dict__)


class Screen(JsonSerializableMixIn):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        check_value(width, 'width')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        check_value(height, 'height')
        self._height = height

    @property
    def resolution(self):
        return self.width * self.height

    def __len__(self):
        return self.width


# 测试:
s = Screen(1024, 768)
# print(len(s))
# print(s.to_json())

# a,*b,c = 'python'
# print(a,b,c)

# a,*b,c = ['a','b','c','d']
# print(a,b,c)

# a,*b,c = ('a','b','c','d')
# print(a,b,c)

# a,*b,c = {'a':1,'b':2,'c':3}.values()
# print(a,b,c)

# a,*b,c = {'a':1,'b':2,'c':3}.keys()
# print(a,b,c)

# a, *b, c = 123456,2,3
# print(a, b, c)
