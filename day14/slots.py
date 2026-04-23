from types import MethodType


class Student:
    __slots__ = ['count','set_count'] #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    pass



a = Student()

a.count = 1

def _set_count(self):
    self.count += 1

a.set_count = MethodType(_set_count,a)

a.set_count()

print(a.count)

Student.set_count = _set_count # 给class绑定方法

a2 = Student()

a2.count = 5

a2.set_count()

print(a2.count)