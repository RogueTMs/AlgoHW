from math import inf


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower, upper):

            if not node:
                return True

            if lower < node.val < upper:
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

            else:
                return False

        return helper(node=root, lower=-inf, upper=inf)
