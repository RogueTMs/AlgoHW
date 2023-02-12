from math import pow
from random import randint


def mult(x, y):
    l_x = len(x)
    l_y = len(y)
    if l_x == l_y and l_x == 1:
        return int(x) * int(y)

    n = max(l_x, l_y)
    if n % 2 != 0:
        n += 1
    x = '0' * (n - l_x) + x
    y = '0' * (n - l_y) + y
    n //= 2

    a = x[:n:]
    b = x[n::]
    c = y[:n:]
    d = y[n::]

    first = mult(a, c)
    second = mult(b, d)
    third = mult(str((int(a) + int(b))), str((int(c) + int(d)))) - first - second

    return int(int(first) * pow(10, (2*n)) + int(third) * pow(10, n) + int(second))


def test(depth):
    for i in range(depth):
        a = randint(1, 10000000)
        b = randint(1, 10000000)
        if a * b != mult(str(a), str(b)):
            print(a, b)
            return 'Alert!'
    return 'Fine'


print(test(1000))

