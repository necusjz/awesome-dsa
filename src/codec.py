from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Codec:
    @staticmethod
    def serialize(root):
        if not root:
            return []
        data = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                data.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                # use `#` to represent empty node
                data.append("#")
        return data

    @staticmethod
    def deserialize(data):
        if not data:
            return None
        # reconstruct from root node
        root = TreeNode(data[0])
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if data[idx] != "#":
                node.left = TreeNode(data[idx])
                queue.append(node.left)
            idx += 1
            if data[idx] != "#":
                node.right = TreeNode(data[idx])
                queue.append(node.right)
            idx += 1
        return root
