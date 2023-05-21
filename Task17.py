class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        cur = head
        prev = None

        for _ in range(left - 1):
            prev = cur
            cur = cur.next

        last = prev
        new_end = cur

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        new_end.next = cur

        if last:
            last.next = prev
        else:
            head = prev

        return head
