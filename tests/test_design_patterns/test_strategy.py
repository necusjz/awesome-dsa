from src.design_patterns.strategy import Values


def test_strategy():
    values = Values([-7, -4, -1, 0, 2, 6, 9])

    assert values.filter(lambda x: x < 0) == [0, 2, 6, 9]
    assert values.filter(lambda x: x & 1) == [-4, 0, 2, 6]
