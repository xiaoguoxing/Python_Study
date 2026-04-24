# assert logging


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


if __name__ == '__main__':
    # foo('0')
    pass

import logging

logging.basicConfig(level=logging.WARNING)
s = '0'
n = int(s)
logging.info('n = %d' % n)
logging.debug('n = %d' % n)
logging.warning('n = %d' % n)
logging.error('n = %d' % n)
print(10 / n)
