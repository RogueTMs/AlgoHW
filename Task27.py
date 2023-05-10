class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        res = []

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in seen:
                if not seen[sequence]:
                    seen[sequence] = True
                    res.append(sequence)
            else:
                seen[sequence] = False

        return res