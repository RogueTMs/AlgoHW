class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        z_pos = -1
        t_pos = len(nums)
        i = 0

        while i < t_pos:
            print(nums, i)
            if nums[i] == 0:
                z_pos += 1
                nums[i], nums[z_pos] = nums[z_pos], nums[i]
            elif nums[i] == 2:
                t_pos -= 1
                nums[i], nums[t_pos] = nums[t_pos], nums[i]
                i -= 1
            i += 1

