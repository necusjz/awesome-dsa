import random

from src.heap_sort import heap_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort


def test_heap_sort():
    nums = [random.randint(1, 1000) for _ in range(1000)]
    heap_sort(nums)

    assert nums == sorted(nums)


def test_merge_sort():
    nums = [random.randint(1, 1000) for _ in range(1000)]
    merge_sort(nums)

    assert nums == sorted(nums)


def test_quick_sort():
    nums = [random.randint(1, 1000) for _ in range(1000)]
    quick_sort(nums)

    assert nums == sorted(nums)
