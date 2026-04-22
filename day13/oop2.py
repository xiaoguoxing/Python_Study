# 继承和多态
class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run Animal')


class Dog(Animal):
    def run(self):
        print(f'run Dog{self.name}')


class Cat(Animal):
    def run(self):
        print(f'run Cat')


dog = Dog('Dog')
cat = Cat('Cat')
dog.run()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))


def run_twice(func):
    if isinstance(func, Animal):
        func.run()
    if hasattr(func, 'run'):
        print('有run')
run_twice(Dog('dog 1111'))
