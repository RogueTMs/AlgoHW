import random


def counting_sort(arr, ind):
    buff = [0 for i in range(256)]
    ans = [0 for i in range(len(arr))]
    for i in arr:
        num = ord(i[ind])
        buff[num] += 1

    for i in range(1, 256):
        buff[i] += buff[i - 1]

    for i in range(len(arr) - 1, -1, -1):

        num = ord(arr[i][ind])
        buff[num] -= 1
        ans[buff[num]] = arr[i]

    return ans


def radix(arr):
    for i in range(len(arr[0]) - 1, -1, -1):
        arr = counting_sort(arr, i)
    return arr


def test():
    size = 1000
    deep = 10000
    mas = []

    for j in range(deep):
        word = ''
        for i in range(size):
            c = chr(random.randint(0, 255))
            word += c
        mas.append(word)
    print(mas)
    if sorted(mas) == radix(mas):
        print('Успех')


test()