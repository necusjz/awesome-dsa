def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y
