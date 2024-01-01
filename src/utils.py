class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val
