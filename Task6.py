def wiggleSort(nums) -> None:
    def mergeSort(array):
        if len(array) > 1:

            r = len(array) // 2
            L = array[:r]
            M = array[r:]

            mergeSort(L)
            mergeSort(M)

            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1

    mergeSort(nums)
    cpy = nums.copy()
    for i in range(1, len(nums), 2):
        nums[i] = cpy.pop()
    for i in range(0, len(nums), 2):
        nums[i] = cpy.pop()

