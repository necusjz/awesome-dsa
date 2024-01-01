from src.next_permutation import next_permutation


def test_next_permutation():
    nums = [1, 2, 3, 6, 5, 4]

    assert next_permutation(nums) == [1, 2, 4, 3, 5, 6]
