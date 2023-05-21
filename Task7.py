from math import ceil


class Solution:
    def sortArray(self, nums):

        def swap(left, right):
            nums[left], nums[right] = nums[right], nums[left]

        def merge(first_from, first_to, second_from, second_to, buff_from, buff_to):
            print(nums[first_from:first_to], nums[second_from:second_to], nums[buff_from:buff_to])
            i, j, k = first_from, second_from, buff_from
            while k < buff_to and i < first_to and j < second_to:

                if nums[i] <= nums[j]:
                    swap(k, i)
                    i += 1
                else:
                    swap(k, j)
                    j += 1
                k += 1

            while j < second_to:
                swap(k, j)
                j += 1
                k += 1
            while i < first_to:
                swap(k, i)
                k += 1
                i += 1

        def merge_sort(_from, to, buff_from, buff_to):
            # print('JUST MERGE_SORT - ', nums[_from: to], nums[buff_from: buff_to])
            if to - _from <= 2: return
            if to - _from == 3:
                if nums[_from] > nums[to - 1]:
                    swap(_from, to - 1)
                return

            mid = (_from + (to - _from) // 2)
            coef = to - mid
            merge_sort(_from, mid, buff_from, buff_to - coef)
            merge_sort(mid, to, buff_from + coef, buff_to)

            merge(_from, mid, mid, to, buff_from, buff_to)
            # print(nums[buff_from: buff_to])
            for i in range(to - _from):
                swap(_from + i, buff_from + i)
            # print("RES - ", nums[_from: to])

        def merge_sort_in_place(_from, to):
            print(_from, to)
            if to - _from <= 2: return
            if to - _from == 3:
                print("YEAH")
                if nums[_from] > nums[to - 1]:
                    swap(_from, to - 1)
                return
            mid = (_from + to) // 2
            half_mid = (_from + mid) // 2
            # mid = ceil((_from + to) / 2)
            # half_mid = ceil((mid + _from) / 2)

            merge_sort_in_place(_from, half_mid)
            merge_sort_in_place(half_mid, mid)

            # if to - mid < half_mid - _from + mid - half_mid:
            #     merge(_from + 1, half_mid, half_mid, mid, mid, to)
            #     for i in range(_from, to - mid + 1):
            #         if nums[i] > nums[mid + i - 1]:
            #             swap(i, mid + i - 1)
            #         else:
            #             break
            # else:
            merge(_from, half_mid, half_mid, mid, mid, to)
            # merge(_from, to, mid, half_mid)

            print('BEFORE - ', nums[_from: to], _from, to)

            while mid - half_mid > 0:
                if mid - half_mid < half_mid - _from:
                    mid += 1
                merge_sort(_from, half_mid, half_mid, mid)
                # print('AFTER - ', nums[_from: half_mid], _from, to, '\n')

                merge(_from, half_mid, mid, to, half_mid, to)
                # print('AFTER ALL - ', nums[_from: to], _from, to, '\n')
                mid = half_mid
                half_mid = (mid + _from) // 2
                # print(_from, half_mid, mid)

            for i in range(_from, to - 1):
                if nums[i] > nums[i + 1]:
                    swap(i, i + 1)
                else:
                    break

            print('END - ', nums[_from: to], _from, to, '\n')

        merge_sort_in_place(0, len(nums))
        return nums


nums = [-96, -70, -83, -84, -25, 30, -74, -24, -20, -5, 1, 0, 5, -98, 11]
# nums = [-96, -91, -90, -84, -74, 30, -25]


# nums = [-96, -91, -90, -84, -74, -30, -25, -24, -20, -5, -3, -2, 2, -9, 2, 10, -11, 11, 30, -44, 48, -22, 28, -87, -78,
#         -74, -71, -58, 54, 25, 34, 35, 50, 50, 51, 63, 13, 16, 21, 64, 8, 10, 26, 29, -10, -8, -72, -55, -46, -28, -6,
#         65, -20, 80, -24, 73, 85, 55, 92, 77, 93, 12, 52, 56, 95, -12, -2, 57, 65, -44, -28, -84, -68, -63, 98, 26, 37,
#         72, 86, 86, 91, 92, 45, 47, 57, 29, 35, -85, -69, -56, -46, -45, -39, -13, -13, 14, 23, 25]

sol = Solution()
print(sol.sortArray(nums))

