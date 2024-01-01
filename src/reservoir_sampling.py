import random


def reservoir_sampling(nums, k):
    sampled = []
    for i in range(k):
        sampled.append(nums[i])

    for j in range(k, len(nums)):
        idx = random.randint(0, j)
        if idx < k:
            sampled[idx] = nums[j]

    return sampled
