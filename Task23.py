from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def solve(node, lesser, greater):
            if not node:
                return True
            if lesser < node.val < greater:
                return solve(node.left, lesser, node.val) and solve(node.right, node.val, greater)
            else:
                return False

        return solve(root, -inf, inf)
