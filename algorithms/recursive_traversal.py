class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traversal:
    @staticmethod
    def pre_order(root):
        ret = []
        def dfs(node):
            if not node:
                return
            ret.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ret

    @staticmethod
    def in_order(root):
        ret = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)
        dfs(root)
        return ret

    @staticmethod
    def post_order(root):
        ret = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ret.append(node.val)
        dfs(root)
        return ret
