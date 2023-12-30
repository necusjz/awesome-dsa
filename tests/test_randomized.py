from src.fisher_yates import fisher_yates
from src.reservoir_sampling import reservoir_sampling


def test_fisher_yates():
    nums = list(range(1000))
    shuffled = fisher_yates(nums)

    assert len(shuffled) == len(nums)
    assert shuffled != nums


def test_reservoir_sampling():
    nums = list(range(1000))
    samples = [reservoir_sampling(nums, 5) for _ in range(10)]

    assert any(samples[i] != samples[i+1] for i in range(len(samples) - 1))
