import sys

'test module'

__author__ = "GuoXing Wu"

abc = list(range(1,10))

def test():
    args = sys.argv
    if len(args) == 1:
        print(f'hello {args[0]}')
    elif len(args) == 2:
        print(f'hello {args[1]}')
    else:
        print('Too many arguments')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    test()
