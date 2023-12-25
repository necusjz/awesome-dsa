def kadane(nums):
    ret = 0

    curr_max = 0
    for num in nums:
        curr_max += num
        curr_max = max(0, curr_max)

        ret = max(ret, curr_max)

    return ret
