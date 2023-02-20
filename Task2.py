from random import randint

def mult(x, y):
    l_x = len(str(x))
    l_y = len(str(y))

    dif = abs(l_x - l_y)

    if l_y == 1 or l_x == 1:
        return x * y

    n = l_x

    if n % 2 != 0:
        n += 1
        l_x *= 10
        l_y *= 10

    n //= 2

    a = int(x // (10**n))
    b = int(x % (10**n))
    c = int(y // (10**n))
    d = int(y % (10**n))

    first = mult(a, c)
    second = mult(b, d)
    third = mult(a + b, c + d) - first - second

    return first * 10**(2 * n) + third * 10**n + second


def test_kar(a, b):
    assert mult(a, b) == a * b


def test(depth):
    for i in range(depth):
        a = randint(1, 100000000000000)
        b = randint(1, 100000000000000)
        if a * b != mult(a, b):
            print(a, b)
            return 'Alert!'
    return 'Fine'


print(test(1000))
print(mult(0, 12))
test_kar(1098765432345678765434567, 123456789098765432345678909876)

