# В merge приходит массив, поделённый на sorted и not sorted.
# Делим not sorted пополам и сортируем одну половину
# Дальше мержим две отсортированные части, как буффер S + Q

def sortArray(nums):
    merge_sort_in_place(nums, 0, len(nums))
    return nums


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def merge(A, start, mid, end):
    L = A[start:mid]
    R = A[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k, end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1


def merge_sort_in_place(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        merge_sort_in_place(A,p,mid)
        merge_sort_in_place(A,mid,r)
        merge(A,p,mid,r)


nums = [5, 2, 3, 1]
print(sortArray(nums))
