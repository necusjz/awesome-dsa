class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traversal:
    def __init__(self):
        self.ret = []

    def pre_order(self, root):
        if not root:
            return root
        self.ret.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)
        return self.ret

    def in_order(self, root):
        if not root:
            return root
        self.in_order(root.left)
        self.ret.append(root.val)
        self.in_order(root.right)
        return self.ret

    def post_order(self, root):
        if not root:
            return root
        self.post_order(root.left)
        self.post_order(root.right)
        self.ret.append(root.val)
        return self.ret
