def sortArray(nums):
    return merge_sort(nums)


def merge(left, right, res):
    lsize, rsize = len(left), len(right)
    n = lsize + rsize
    assert n == len(res)
    i, j, k = 0, 0, 0
    while k < n and i < lsize and j < rsize:
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1

    while i < lsize:
        res[k] = left[i]
        k += 1
        i += 1
    while j < rsize:
        res[k] = right[j]
        k += 1
        j += 1


def merge_sort(array):
    if len(array) == 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    middle = len(array) // 2
    l = merge_sort(array[:middle])
    r = merge_sort(array[middle:])

    buffer = [0 for i in range(len(array))]
    merge(l, r, buffer)

    for i in range(0, len(array)):
        array[i] = buffer[i]

    return array


nums = [5,2,3,1]
print(sortArray(nums))