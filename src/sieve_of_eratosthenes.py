def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # initialize boolean array

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # update all multiples of p
            for idx in range(p * p, n + 1, p):
                is_prime[idx] = False

        p += 1

    ret = []
    for p in range(2, n + 1):
        if is_prime[p]:
            ret.append(p)
    return ret
