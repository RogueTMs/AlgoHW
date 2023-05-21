# Definition for singly-linked list.
from heapq import heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        t = self
        s = ""
        while t is not None:
            s += f"{t.val} "
            t = t.next
        s = s.strip()
        s = s.replace(" ", "->")
        return s

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __le__(self, other):
        return self.val < other.val or self.val == other.val


class BinHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def __str__(self):
        return self.heapList.__str__()

    def size(self):
        return self.size

    def get_parent(self, ind):
        if self.size > 0 and ind > 0:
            return (ind - 1) // 2
        else:
            return None

    def _sift_up(self, ind):
        p = self.get_parent(ind)
        if p is not None:
            while p is not None and self.heapList[ind] < self.heapList[p]:
                self.heapList[ind], self.heapList[p] = self.heapList[p], self.heapList[ind]
                ind = p
                p = self.get_parent(ind)

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self._sift_up(self.size - 1)

    def _sift_down(self, ind):
        mc = self.get_min_child(ind)
        if mc is not None:
            while mc is not None and self.heapList[ind] > self.heapList[mc]:
                self.heapList[ind], self.heapList[mc] = self.heapList[mc], self.heapList[ind]
                ind = mc
                mc = self.get_min_child(ind)

    def peek_min(self):
        return self.heapList[0]

    def get_min(self):
        if self.size > 0:
            self.heapList[0], self.heapList[-1] = self.heapList[-1], self.heapList[0]
            d = self.heapList.pop()
            self.size -= 1
            self._sift_down(0)
            return d

    def get_min_child(self, i):
        if 2 * i + 1 < self.size:
            if i * 2 + 2 >= self.size:
                return i * 2 + 1
            else:
                if self.heapList[2 * i + 1] <= self.heapList[2 * i + 2]:
                    return 2 * i + 1
                else:
                    return 2 * i + 2
        else:
            return None

    def buildHeap(self, list):
        self.size = len(list)
        i = (self.size - 1) // 2
        self.heapList = list
        for i in range(i, -1, -1):
            self._sift_down(i)





class Solution:
    def mergeKLists(self, lists):
        heap = BinHeap()
        heap.buildHeap([node for node in lists])
        new_list = ListNode()
        head = new_list
        first = False
        while heap.heapList:
            tmp = heap.get_min()
            if not first:
                head.val = tmp.val
                first = True
            else:
                head.next = tmp
                head = head.next
            if tmp.next is not None:
                heap.insert(tmp.next)
        return new_list


test_list1 = ListNode(val=1)
start = test_list1
for i in range(2, 7):
    new_node = ListNode(val=i)
    start.next = new_node
    start = start.next

test_list3 = ListNode(val=7)
start = test_list3
for i in range(10, 15):
    new_node = ListNode(val=i)
    start.next = new_node
    start = start.next

test_list2 = ListNode(val=9)
start = test_list2
for i in range(10, 11):
    new_node = ListNode(val=i)
    start.next = new_node
    start = start.next

print(test_list1, test_list2, test_list3, sep="\n")

mas = [test_list1, test_list2, test_list3]

sol = Solution()
print(sol.mergeKLists(lists=mas))
