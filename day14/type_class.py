# type()

Hello = type('Hello', (object,), dict(say=lambda self, say: print(say), abc='defg'))
h = Hello()
h.say(h.abc)


# metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


list1 = MyList()
list1.add(1)

print(list1)
