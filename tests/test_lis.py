from src.lis import longest_increasing_subsequence


def test_lis():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    assert longest_increasing_subsequence(nums) == 4
