def hIndex(citations) -> int:
    enumerates = [1, 4, 10, 23, 57, 132, 301, 701]
    for k in enumerates:
        if k < len(citations):
            for i in range(k, len(citations)):
                j = i
                while j - k >= 0 and citations[j - k] > citations[j]:
                    citations[j - k], citations[j] = citations[j], citations[j - k]
                    j -= k

    for i in range(len(citations) - 1, -1, -1):
        if citations[i] <= len(citations) - i:
            return max(citations[i], len(citations) - i - 1)
    return min(len(citations), citations[0])

