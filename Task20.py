class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MinStack:
    def __init__(self):
        self.head = None
        self.min = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

        if not self.min or self.min.val >= val:
            old_min = self.min
            self.min = Node(val)
            self.min.next = old_min

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head
            self.head = self.head.next

            if self.min.val == value.val:
                old_min = self.min
                self.min = old_min.next

            return value.val

    def top(self):
        if self.head is None:
            return None
        return self.head.val

    def getMin(self):
        return self.min.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
