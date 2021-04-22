class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traversal:
    @staticmethod
    def pre_order(root):
        if not root:
            return root
        ret = []
        stack, node = [], root
        while stack or node:
            if node:
                ret.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return ret

    @staticmethod
    def in_order(root):
        if not root:
            return root
        ret = []
        stack, node = [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ret.append(node.val)
                node = node.right
        return ret

    @staticmethod
    def post_order(root):
        if not root:
            return root
        ret = []
        stack, node = [], root
        while stack or node:
            if node:
                ret.append(node.val)
                stack.append(node)
                # go right first, then reverse its result
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return ret[::-1]
