import math


def sortArray(nums):
    merge_sort_in_place(0, len(nums) - 1)
    return nums


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def merge(start, end):
    gap = end - start + 1
    if gap <= 1:
        gap = 0
    else:
        gap = int(math.ceil(gap / 2))

    while gap > 0:
        i = start
        while (i + gap) <= end:
            j = i + gap

            if nums[i] > nums[j]:
                swap(nums, i, j)

            i += 1

        if gap <= 1:
            gap = 0
        else:
            gap = int(math.ceil(gap / 2))


def merge_sort_in_place(s, e):
    if s == e:
        return

    mid = (s + e) // 2

    merge_sort_in_place(s, mid)
    merge_sort_in_place(mid + 1, e)

    merge(s, e)


#
#
# def merge(_from, to, mid, usmid):
#     print(nums[_from:mid], nums[usmid:to], nums[_from:usmid + 1])
#     lsize, rsize = mid, to
#     n = _from + mid - _from + to - usmid
#     # print('n - ', n)
#     # assert n == len(res)
#     i, j, k = _from, usmid, _from
#     while k < n and i < lsize and j < rsize:
#         # print(nums, i, nums[i], j, nums[j])
#         if nums[i] <= nums[j]:
#             swap(nums, k, i)
#             # nums[_from + k] = nums[_from + i]
#         else:
#             swap(nums, k, j)
#             # nums[_from + k] = nums[usmid + j]
#             # j += 1
#         i += 1
#         k += 1
#
#     while j < rsize:
#         swap(nums, k, j)
#         j += 1
#         k += 1
#
#     # print(nums)
#     # while i < lsize:
#     #     k += 1
#     #     i += 1
#     #     print(k, j, i, mid, to)
#     #     swap(nums, k, i)
#     # while j < rsize:
#     #     k += 1
#     #     j += 1
#     #     print('grg')
#     #     print(k, j, i, mid, to)
#     #     swap(nums, k, j)
#
#
# def merge_sort_in_place(_from, to, buffer):
#     print(_from, to, nums[_from: to])
#     if to - _from == 1: return
#     if to - _from == 2:
#         if nums[_from] > nums[to - 1]:
#             swap(nums, _from, to - 1)
#         return
#
#     mid = int((_from + to) / 2)
#     usmid = int((mid + to) / 2)
#
#     merge_sort_in_place(_from, mid, buffer)
#     merge_sort_in_place(mid, to, buffer)
#     print('back', nums[_from: to])
#     merge(_from, to, mid, usmid)
#     print('after merge - ', nums)
#
#     # if to - usmid == 1:
#     #     i = usmid
#     #     while i != _from and nums[i] < nums[i - 1]:
#     #         swap(nums, i, i - 1)
#     #         i -= 1
#     i = to - 1
#     while i != _from and nums[i] < nums[i - 1]:
#         swap(nums, i, i - 1)
#         i -= 1
#
#
#     print('Here another one - ', nums[_from:to])
#     mid = usmid
#     usmid = int((mid + to) / 2)
#     merge_sort_in_place(mid, to, buffer)
#     print('end main loop - ', nums[_from:to])
#     merge(_from, to, mid, usmid)
#
#     i = to - 1
#     while i != _from and nums[i] < nums[i - 1]:
#         swap(nums, i, i - 1)
#         i -= 1
#
#
#     print(nums)


nums = [-96, -91, -90, -84, -74, -30, -25, -24, -20, -5, -3, -2, 2, -9, 2, 10, -11, 11, 30, -44, 48, -22, 28, -87, -78,
        -74, -71, -58, 54, 25, 34, 35, 50, 50, 51, 63, 13, 16, 21, 64, 8, 10, 26, 29, -10, -8, -72, -55, -46, -28, -6,
        65, -20, 80, -24, 73, 85, 55, 92, 77, 93, 12, 52, 56, 95, -12, -2, 57, 65, -44, -28, -84, -68, -63, 98, 26, 37,
        72, 86, 86, 91, 92, 45, 47, 57, 29, 35, -85, -69, -56, -46, -45, -39, -13, -13, 14, 23, 25]
sortArray(nums)
print(nums)
