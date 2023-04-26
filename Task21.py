# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root == None:
            return "x"
        return "[" + str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right) + "]"

    def deserialize(self, data):
        if data == "x":
            return None
        else:
            # val
            val = int(data[1:data.find(",")])

            # left
            leftstart = data.index(',') + 1
            if data[leftstart] == "x":
                leftend = leftstart + 1
            else:
                leftend = 0
                co = 1
                for i in range(leftstart + 1, len(data)):
                    if co == 0:
                        leftend = i
                        break
                    elif data[i] == "[":
                        co += 1
                    elif data[i] == "]":
                        co -= 1
            # right
            if data[leftend + 1] == "x":
                right = None
            else:
                r = data[leftend + 1:len(data) - 1]
                right = self.deserialize(r)

        return TreeNode(val, self.deserialize(data[leftstart:leftend]), right)
