def hIndex(citations) -> int:
    enumerates = [(((3**x) - 1) // 2) for x in range(1000)]
    for k in enumerates:
        if k < len(citations):
            for i in range(k, len(citations)):
                j = i
                while j - k >= 0 and citations[j - k] > citations[j]:
                    citations[j - k], citations[j] = citations[j], citations[j - k]
                    j -= k
        else:
            break

    for i in range(len(citations) - 1, -1, -1):
        if citations[i] <= len(citations) - i:
            return max(citations[i], len(citations) - i - 1)
    return min(len(citations), citations[0])


