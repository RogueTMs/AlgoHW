class FreqStack:
    def __init__(self):
        self.nums = {}
        self.dict = {}
        self.max = -1

    def push(self, val):
        if val in self.nums.keys():
            self.nums[val] += 1
        else:
            self.nums[val] = 1

        if self.nums[val] in self.dict.keys():
            self.dict[self.nums[val]].append(val)
        else:
            self.dict[self.nums[val]] = [val]

        self.max = max(self.max, self.nums[val])

    def pop(self):
        if len(self.nums.keys()) == 0:
            return None
        else:
            ans = self.dict[self.max].pop()
            self.nums[ans] -= 1
            if self.nums[ans] == 0:
                del self.nums[ans]

            if len(self.dict[self.max]) == 0:
                del self.dict[self.max]
                self.max -= 1
            return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()