import random


def reservoir_sampling(nums, k):
    ret = []
    for i in range(k):
        ret.append(nums[i])

    for j in range(k, len(nums)):
        idx = random.randint(0, j)
        if idx < k:
            ret[idx] = nums[j]

    return ret
