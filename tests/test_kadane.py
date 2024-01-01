from src.kadane import kadane


def test_kadane():
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]

    assert kadane(nums) == 7
