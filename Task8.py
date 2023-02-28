def solve(nums):
    count = 0
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
           count += 1

    res = sort_and_count_inversions(nums)

    return res[0] == count


def sort_and_count_inversions(array):
    if len(array) == 1:
        return [0, array]

    middle = len(array) // 2
    left = sort_and_count_inversions(array[:middle])
    right = sort_and_count_inversions(array[middle:])

    buffer = [-1 for i in range(len(array))]
    mas = merge_and_count_split(left[1], right[1], buffer)[0]
    for i in range(0, len(array)):
        array[i] = buffer[i]

    return [left[0] + right[0] + mas, array]


def merge_and_count_split(left, right, res):
    lsize, rsize = len(left), len(right)
    n = lsize + rsize
    assert n == len(res)
    i, j, k, ans = 0, 0, 0, 0
    while k < n and i < lsize and j < rsize:
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
            ans += lsize - i
        k += 1

    while i < lsize:
        res[k] = left[i]
        k += 1
        i += 1
    while j < rsize:
        res[k] = right[j]
        k += 1
        j += 1

    return [ans, res]


print(solve([1, 0]))
print(solve([1, 2, 0]))