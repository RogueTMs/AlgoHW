def solve(n, m: str) -> (int, int):
    ans = []
    cur = n[0]
    n = n[1::]
    while n:
        if cur == '0':
            ans.append(0)
            cur = n[0]
            n = n[1::]
        elif int(cur) < int(m):
            cur += n[0]
            n = n[1::]
        else:
            cur, i = enumeration(cur, m)
            ans.append(i)

            if int(cur):
                cur += n[0]
            else:
                cur = n[0]

            n = n[1::]

    cur, i = enumeration(cur, m)
    ans.append(i)

    return int("".join(map(str, ans))), int(cur)


def enumeration(dividend, divisor):
    for i in range(1, 10):
        if int(divisor) * i >= int(dividend):
            if int(divisor) * i != int(dividend):
                i -= 1
            dividend = str(int(dividend) - (int(divisor) * i))
            return dividend, i


print(solve('358', '17'))
print(solve('1000', '2'))
print(solve('1', '17'))


