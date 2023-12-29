from src.newton import sqrt


def test_newton():
    a = 327

    assert sqrt(a) == int(a ** 0.5)
