# 定制类
class Screen:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Screen width: {self.width}, height: {self.height}'
    __repr__ = __str__



class Screen2:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        if self.count>=10:
            raise StopIteration()
        return self.count


for i in Screen2():
    print(i)