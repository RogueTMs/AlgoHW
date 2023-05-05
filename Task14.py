class Solution:
    def findKthLargest(self, nums, k):
        from random import randint

        def partition(arr):

            if len(arr) == 1:
                return [], arr[0], []
            if len(arr) == 2:
                if arr[0] <= arr[1]:
                    return [], arr[0], arr[1]
                else:
                    return [], arr[1], arr[0]

            p = randint(0, len(arr) - 1)
            pivot = arr[p]
            right = []
            left = []
            for i in range(len(arr)):
                if not i == p:
                    if arr[i] > pivot:
                        right.append(arr[i])
                    else:
                        left.append(arr[i])
            return left, pivot, right

        def kth(arr, k):

            (left, pivot, right) = partition(arr)
            if type(right) is int:
                right = [right]
            if len(right) == k - 1:
                result = pivot
            elif len(right) > k - 1:
                result = kth(right, k)
            else:
                result = kth(left, k - len(right) - 1)
            return result

        kth(nums, k)


sol = Solution()
sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
