from src.cycle_sort import min_swap


def test_min_swap():
    nums = [101, 758, 315, 730, 472, 619, 460, 479]

    assert min_swap(nums) == 5
