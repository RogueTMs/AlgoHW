def wiggleSort(nums) -> None:
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr.copy()
        else:
            right, left, equal = [], [], []
            cur = arr[len(arr) // 2]
            for i in arr:
                if i > cur:
                    right.append(i)
                elif i < cur:
                    left.append(i)
                else:
                    equal.append(i)

            return quick_sort(left) + equal + quick_sort(right)

    cpy = quick_sort(nums)
    for i in range(1, len(nums), 2):
        nums[i] = cpy.pop()
    for i in range(0, len(nums), 2):
        nums[i] = cpy.pop()
