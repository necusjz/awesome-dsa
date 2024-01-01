def sieve_of_eratosthenes(num):
    is_prime = [True] * (num + 1)

    p = 2
    while p * p <= num:
        if is_prime[p]:
            for i in range(p * p, num + 1, p):  # update multiples of p
                is_prime[i] = False

        p += 1

    primes = []
    for p in range(2, num + 1):
        if is_prime[p]:
            primes.append(p)

    return primes
