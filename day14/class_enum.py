# 枚举类
from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(f'{name}=>{member.value}')

@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

week_day = WeekDay
print(week_day.Sun)
print(week_day.Sun.value)
print(week_day.Sun==WeekDay.Sun)
print(WeekDay(1))
print(week_day.Mon==WeekDay(1))
# for name, member in week_day.__members__.items():
#     print(f'{name}=>{member.value}')


from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
