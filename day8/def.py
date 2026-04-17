def my_abs(number):
    if not isinstance(number, (int, float)):
        raise TypeError('bad operand type')
    if number >= 0:
        return number
    else:
        return -number


print(my_abs(-99))


def pas():
    pass  #占位符没想好怎么写就先写pass


def init():
    x = 1
    y = 2
    z = 3
    return x, y, z


(x1, y1, z1) = init()
print(y1)
