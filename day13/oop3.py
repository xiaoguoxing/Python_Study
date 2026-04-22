# class Student(object):
#     age = 20
#     def __init__(self, name):
#         self.name = name
#
# s = Student('Bob')
# s.score = 90


def _set_count():
    Student.count += 1


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        _set_count()


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
