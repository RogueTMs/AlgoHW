# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def storeBSTNodes(self, root, treeNodes):
        if not root:
            return
        self.storeBSTNodes(root.left, treeNodes)
        treeNodes.append(root)
        self.storeBSTNodes(root.right, treeNodes)

    def buildBalancedBST(self, treeNodes, startIdx, endIdx):
        if startIdx > endIdx:
            return None
        mid = (startIdx + endIdx) // 2
        root = treeNodes[mid]
        root.left = self.buildBalancedBST(treeNodes, startIdx, mid - 1)
        root.right = self.buildBalancedBST(treeNodes, mid + 1, endIdx)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        treeNodes = []
        self.storeBSTNodes(root, treeNodes)
        startIdx = 0
        endIdx = len(treeNodes) - 1
        return self.buildBalancedBST(treeNodes, startIdx, endIdx)
