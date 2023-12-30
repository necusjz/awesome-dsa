from src.codec import Codec


def test_codec():
    data = [1, 2, 3, "#", "#", 4, 5, "#", "#", "#", "#"]
    root = Codec.deserialize(data)

    assert Codec.serialize(root) == data
