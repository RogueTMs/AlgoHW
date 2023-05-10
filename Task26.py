from _collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq_numList_dict = defaultdict(list)
        self.num_freq_dict = defaultdict(int)
        self.max_frequency = 0

    def push(self, x: int) -> None:
        self.num_freq_dict[x] += 1
        cur_frequency = self.num_freq_dict[x]
        self.max_frequency = max(self.max_frequency, self.num_freq_dict[x])
        self.freq_numList_dict[cur_frequency].append(x)

    def pop(self) -> int:
        high_freq_last_element = self.freq_numList_dict[self.max_frequency].pop()
        self.num_freq_dict[high_freq_last_element] -= 1

        if not self.freq_numList_dict[self.max_frequency]:
            self.max_frequency -= 1

        return high_freq_last_element

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()