from src.euclid import gcd, lcm, gcd_extended


def test_euclid():
    a, b = 14, 8
    result, x, y = gcd_extended(a, b)

    assert gcd(a, b) * lcm(a, b) == a * b
    assert a * x + b * y == result
