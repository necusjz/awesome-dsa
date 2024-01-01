import random


def fisher_yates(nums):
    shuffled = nums[:]
    for i in range(len(shuffled) - 1, 0, -1):
        idx = random.randint(0, i)
        shuffled[idx], shuffled[i] = shuffled[i], shuffled[idx]

    return shuffled
