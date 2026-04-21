class Study(object):
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print(f'{self.name}:{self.score}')

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

a = Study('wu',100)
b = Study('zhangsan',50)
print(b.get_grade())

c = 50
if 0<=c<=100:
    print('1111')
