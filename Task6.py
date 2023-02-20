def wiggleSort(nums) -> None:
    enumerates = [1, 4, 10, 23, 57, 132, 301, 701]
    for k in enumerates:
        if k < len(nums):
            for i in range(k, len(nums)):
                j = i
                while j - k >= 0 and nums[j - k] > nums[j]:
                    nums[j - k], nums[j] = nums[j], nums[j - k]
                    j -= k

    print(nums)
    for i in range(1, len(nums) - 1, 2):
        j = i + 1
        while nums[j] <= nums[i]:
            j += 1
            if j == len(nums):
                j -= 1
                break

        nums[i], nums[j] = nums[j], nums[i]


nums = [1, 5, 1, 1, 6, 4]
wiggleSort(nums)
print(nums)
nums = [1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3]
wiggleSort(nums)
print(nums)
