def sqrt(a):
    num = a
    while num * num > a:
        num = (num + a // num) // 2

    return num
