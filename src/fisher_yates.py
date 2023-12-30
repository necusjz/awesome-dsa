import random


def fisher_yates(nums):
    ret = nums[:]
    for i in range(len(ret) - 1, -1, -1):
        idx = random.randint(0, i)
        ret[idx], ret[i] = ret[i], ret[idx]

    return ret
