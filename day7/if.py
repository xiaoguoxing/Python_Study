# If
from unittest import case

age = 12
if age >= 18:
    print(f'{age}>18')
elif age < 18:
    print(f'{age}<18')
else:
    print(f'{age}<18')

birth = 2007  # input('生日是几几年？')
birth = int(birth)

if birth > 2000:
    print('你是00后')
elif birth < 2000:
    print('你是00前')

height = 1.76
weight = 75
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')


source = 'G'
match source:
    case 'A':
        print('him is A')
    case 'B':
        print('him is B')
    case 'C':
        print('him is C')
    case 'D'|'E'|'F':
        print('him is D E F')
    case y if y == 'G':#当source==G时，y=G
        print(f'him is {y}')
    case _: #任意值
        print('him is _')



args = ['gcc','hello.c','hello.py']
match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
    case ['gcc',file1,*files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('error')