# @property

class Student:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age
        # return getattr(self,'_age',10)

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('数字')
        if age < 0 or age > 100:
            raise ValueError('值太大或者太小了0-100')
        self.__age = age


a = Student()
a.age = 40


# print(a.age)
def check_value(value, name):
    if not isinstance(value, int):
        raise TypeError(f'{name}:应为数字')
    if value <= 0:
        raise ValueError(f'{name}:不应该小于0')


class Screen:
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


# 测试:
s = Screen(1024, 768)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
