import random


def fisher_yates(nums):
    for i in range(len(nums) - 1, -1, -1):
        idx = random.randint(0, i)
        nums[idx], nums[i] = nums[i], nums[idx]
