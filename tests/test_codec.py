from src.codec import Codec
from src.utils import TreeNode

root = TreeNode()

root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)


def test_codec():
    data = [0, 1, 2, "#", "#", 3, 4, "#", "#", "#", "#"]

    assert Codec.serialize(root) == data
    assert Codec.deserialize(data) == root
