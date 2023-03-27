from random import randint


def partition(arr, piv):
    i = 0
    j = len(arr) - 1
    num = arr[piv]
    while i < j:
        print(arr, num)
        if arr[i] >= num and arr[j] <= num:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] >= num:
            j -= 1
        elif arr[j] <= num:
            i += 1
        else:
            i += 1
            j -= 1

    return i


def kth(array, k) -> int:
    if len(array) == 1:
        return array[0]

    pivot = randint(0, len(array) - 1)
    p = partition(array, pivot)
    print(array, pivot, p)

    if p + 1 == k:
        return array[p]
    elif p + 1 < k:
        return kth(array[p + 1:], k - p - 1)
    else:
        return kth(array[:p], k)


print(kth([3,2,1,5,6,4], 5))