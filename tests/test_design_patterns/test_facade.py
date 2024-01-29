import pytest

from src.design_patterns.facade import DynamicArray


def test_facade():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)

    assert len(arr) == 3
    assert arr[0] == 1

    with pytest.raises(IndexError):
        _ = arr[3]

    with pytest.raises(IndexError):
        arr.insert(4, 4)

    arr.insert(3, 4)

    assert arr.pop() == 4
    assert arr.pop() == 3
    assert arr.pop() == 2
    assert arr.pop() == 1

    with pytest.raises(SystemError):
        arr.pop()
