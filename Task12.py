from random import randint

class Solution:
    def sortArray(self, nums):
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr.copy()
            else:
                right, left, equal = [], [], []
                cur = arr[randint(0, len(arr) - 1)]
                for i in arr:
                    if i > cur:
                        right.append(i)
                    elif i < cur:
                        left.append(i)
                    else:
                        equal.append(i)

                return quick_sort(left) + equal + quick_sort(right)

        return (quick_sort(nums))