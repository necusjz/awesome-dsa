class SieveOfEratosthenes:
    def __init__(self, n):
        self.n = n

    def sieve(self):
        # initialize boolean array
        is_prime = [True for _ in range(self.n + 1)]
        p = 2
        while p * p <= self.n:
            if is_prime[p]:
                # update all multiples of p
                for i in range(p * p, self.n + 1, p):
                    is_prime[i] = False
            p += 1
        ret = []
        # obtain all prime numbers
        for p in range(2, self.n + 1):
            if is_prime[p]:
                ret.append(p)
        return ret
