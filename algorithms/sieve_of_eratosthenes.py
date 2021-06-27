def sieve_of_eratosthenes(n):
    # initialize boolean array
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            # update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    ret = []
    # obtain all prime numbers
    for p in range(2, n + 1):
        if is_prime[p]:
            ret.append(p)
    return ret
