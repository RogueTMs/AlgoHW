import ctypes


class MyDynMas:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.data = self.make_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, k):
        if not 0 <= k < self.length:
            return IndexError('K is out of bounds !')

        return self.data[k]

    def reallocate(self, old_arr, new_cap):
        new_arr = self.make_array(new_cap)

        for k in range(self.length):
            new_arr[k] = old_arr[k]

        self.data = new_arr

    def add(self, value: int):
        if self.length == self.capacity:
            self.capacity *= 2
            self.reallocate(self.data, self.capacity)

        self.data[self.length] = value
        self.length += 1

    def remove(self):
        if self.length == 0:
            return IndexError('Empty array!')
        self.length -= 1
        if self.length * 4 < self.capacity:
            self.capacity //= 2
            self.reallocate(self.data, self.capacity)

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
