def search(nums: list, target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        cur = (l + r) // 2
        if nums[cur] == target:
            return cur
        elif nums[cur] > target:
            r = cur - 1
        else:
            l = cur + 1

    return -1
