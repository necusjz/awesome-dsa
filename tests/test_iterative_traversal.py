from src.iterative_traversal import prev_order, in_order, post_order
from src.utils import TreeNode

root = TreeNode()

root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)


def test_prev_order():
    assert prev_order(root) == [0, 1, 2, 3, 4]


def test_in_order():
    assert in_order(root) == [1, 0, 3, 2, 4]


def test_post_order():
    assert post_order(root) == [1, 3, 4, 2, 0]
