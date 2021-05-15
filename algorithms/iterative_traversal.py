class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Traversal:
    def __init__(self):
        self.ret = []

    def pre_order(self, root):
        stack, node = [], root
        while stack or node:
            if node:
                self.ret.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return self.ret

    def in_order(self, root):
        stack, node = [], root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.ret.append(node.val)
                node = node.right
        return self.ret

    def post_order(self, root):
        stack, node = [], root
        while stack or node:
            if node:
                self.ret.append(node.val)
                stack.append(node)
                # go right first, then reverse its result
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return self.ret[::-1]
