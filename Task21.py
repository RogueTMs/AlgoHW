class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if root is None:
            return "x"
        return '|'.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        self.ind = 0

        def dfs():
            if data[self.ind] == 'x':
                self.ind += 1
                return None
            node = TreeNode(data[self.ind])
            self.ind += 1
            node.left = dfs()
            node.right = dfs()
            return node

        data = data.split('|')
        return dfs()

