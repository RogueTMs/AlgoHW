class Solution:
    def findRepeatedDnaSequences(self, s):
        seen, ans = {}, []

        for i in range(len(s) - 9):
            arr = s[i:i + 10]
            if arr in seen:
                if not seen[arr]:
                    seen[arr] = True
                    ans.append(arr)
            else:
                seen[sequence] = False

        return ans
