class Solution:
    def sortArray(self, nums):

        def swap(arr, left, right):
            arr[left], arr[right] = arr[right], arr[left]

        def merge(_from, to, mid, usmid):
            print(nums[_from:mid], nums[usmid:to], nums[_from:usmid])
            lsize, rsize = mid, to
            n = _from + mid - _from + to - usmid
            i, j, k = _from, usmid, _from
            while k < n and i < lsize and j < rsize:

                if nums[i] <= nums[j]:
                    swap(nums, k, i)
                    i += 1
                else:
                    swap(nums, k, j)
                    j += 1
                k += 1

            while j < rsize:
                swap(nums, k, j)
                j += 1
                k += 1
            while i < lsize:
                swap(nums, k, i)
                j += 1
                i += 1

        def merge_sort_in_place(_from, to):
            if to - _from == 1: return
            if to - _from == 2:
                if nums[_from] > nums[to - 1]:
                    swap(nums, _from, to - 1)
                return

            mid = int((_from + to) / 2)
            usmid = int((mid + to) / 2)
            print(mid, usmid)

            merge_sort_in_place(_from, mid)
            merge_sort_in_place(mid, to)
            merge(_from, to, mid, usmid)


            print(nums)
            print('BEFORE - ', nums[_from: to], _from, to)

            if to - usmid > 1:
                print('Here')
                usmid += 1
                print(nums[usmid:to])
                # mid = usmid
                # usmid = int((mid + to) / 2)

                merge_sort_in_place(usmid, to)
                merge(_from, to, mid, usmid)

            else:
                i = to - 1
                while i != _from and nums[i] < nums[i - 1]:
                    swap(nums, i, i - 1)
                    i -= 1

            print('AFTER - ', nums[_from: to], _from, to, '\n')

        merge_sort_in_place(0, len(nums))
        return nums


nums = [-96, -91, -90, -84, -74, -30, -25, -24, -20, -5, 1, 0, 5, 98]
# nums = [-96, -91, -90, -84, -74, 30, -25]


# nums = [-96, -91, -90, -84, -74, -30, -25, -24, -20, -5, -3, -2, 2, -9, 2, 10, -11, 11, 30, -44, 48, -22, 28, -87, -78,
#         -74, -71, -58, 54, 25, 34, 35, 50, 50, 51, 63, 13, 16, 21, 64, 8, 10, 26, 29, -10, -8, -72, -55, -46, -28, -6,
#         65, -20, 80, -24, 73, 85, 55, 92, 77, 93, 12, 52, 56, 95, -12, -2, 57, 65, -44, -28, -84, -68, -63, 98, 26, 37,
#         72, 86, 86, 91, 92, 45, 47, 57, 29, 35, -85, -69, -56, -46, -45, -39, -13, -13, 14, 23, 25]
sol = Solution()
print(sol.sortArray(nums))

