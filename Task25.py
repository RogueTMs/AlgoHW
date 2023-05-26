class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     nodes = []
#     root = TreeNode()
#
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#         self.get_nodes(root)
#         for node in self.nodes:
#             self.insert(node)
#         return self.root
#
#     def get_nodes(self, node):
#         if node is None:
#             return
#         else:
#             self.nodes.append(node)
#             self.get_nodes(node.left)
#             self.get_nodes(node.right)
#
#     def balance(self, cur_node, val):
#         if val < cur_node.val:
#             cur_node.left = self.balance(cur_node.left, val)
#         else:
#             cur_node.right = self.balance(cur_node.right, val)
#
#         balance = self.get_balance(cur_node)
#
#         if balance > 1:
#             if self.get_balance(cur_node.left) >= 0:
#                 cur_node = self.rotate_right(cur_node)
#             else:
#                 cur_node = self.rotate_left_right(cur_node)
#         elif balance < -1:
#             if self.get_balance(cur_node.right) <= 0:
#                 cur_node = self.rotate_left(cur_node)
#             else:
#                 cur_node = self.rotate_right_left(cur_node)
#
#         return cur_node
#
#     def insert(self, value):
#         if self.root is None:
#             self.root = TreeNode(value)
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, cur_node):
#         if value < cur_node.val:
#             if cur_node.left is None:
#                 cur_node.left = TreeNode(value)
#             else:
#                 self._insert(value, cur_node.left)
#         elif value > cur_node.val:
#             if cur_node.right is None:
#                 cur_node.right = TreeNode(value)
#             else:
#                 self._insert(value, cur_node.right)
#
#     def rotate_right(self, node):
#         left_temp = node.left
#
#         node.left = left_temp.right
#         left_temp.right = node
#
#         return left_temp
#
#     def rotate_left(self, node):
#         right_temp = node.right
#
#         node.right = right_temp.left
#         right_temp.left = node
#
#         return right_temp
#
#     def rotate_left_right(self, node):
#         node.left = self.rotate_left(node.left)
#
#         return self.rotate_right(node)
#
#     def rotate_right_left(self, node):
#         node.right = self.rotate_right(node.right)
#
#         return self.rotate_left(node)
#
#     def get_balance(self, node):
#         if not node:
#             return 0
#
#         return self.get_height(node.left) - self.get_height(node.right)
#
#     def get_height(self, node):
#         if node is None:
#             return -1
#         else:
#             return max(self.get_height(node.left), self.get_height(node.right)) + 1

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = self.get_nodes(root)
        ans = self.insert(0, len(nodes) - 1, nodes)
        return ans

    def get_nodes(self, node):
        if node is None:
            return []
        else:
            left = self.get_nodes(node.left)
            right = self.get_nodes(node.right)
            return left + [node.val] + right

    def insert(self, _from, to, nodes):
        if _from > to:
            return None

        mid = _from + (to - _from) // 2
        node = TreeNode(nodes[mid])
        node.left = self.insert(_from, mid - 1, nodes)
        node.right = self.insert(mid + 1, to, nodes)

        return node
