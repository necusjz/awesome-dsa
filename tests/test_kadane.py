from src.kadane import kadane


def test_kadane():
    nums1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    nums2 = [-2, -3, -1, -4]

    assert kadane(nums1) == 7
    assert kadane(nums2) == -1
