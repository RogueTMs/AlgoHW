def solve(n, m: int) -> (int, int):
    ans = 0
    nums = [int(x) for x in str(n)]
    cur = 0
    for i in range(len(nums)):
        cur = cur * 10 + nums[i]
        if cur == 0:
            ans = ans * 10
            cur = nums[i]
        elif cur < m:
            pass
        else:
            cur, k = enumeration(cur, m)
            ans = ans * 10 + k

            if cur:
                pass
            else:
                cur = nums[i]

    return ans, cur


def enumeration(dividend, divisor):
    for i in range(1, 10):
        if divisor * i >= dividend:
            if divisor * i != dividend:
                i -= 1
            dividend = dividend - (divisor * i)
            return dividend, i


print(solve(358, 17))
print(solve(1000, 2))
print(solve(1, 17))


