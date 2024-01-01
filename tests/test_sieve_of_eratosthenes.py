from src.sieve_of_eratosthenes import sieve_of_eratosthenes


def test_sieve_of_eratosthenes():
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
