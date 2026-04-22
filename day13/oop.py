class Study(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print(f'{self.__name}:{self.score}')

    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        return self.__name

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


a = Study('wu', 100)
b = Study('zhangsan', 50)
a.print_score()
b.print_score()


# print(a.__name)
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        self.__genders = ['male', 'female']

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in self.__genders:
            self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
