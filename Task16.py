class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        while head != None and head.val != 1000000:
            head.val = 1000000
            head = head.next
        return head
