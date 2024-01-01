from collections import deque

from src.utils import TreeNode


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
                data.append("#")  # use # as empty node

        return data

    @staticmethod
    def deserialize(data):
        if not data:
            return

        root = TreeNode(data[0])  # construct from root node
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
