def kadane(nums):
    max_subarray, curr_max = 0, 0
    for num in nums:
        curr_max += num
        curr_max = max(0, curr_max)

        max_subarray = max(max_subarray, curr_max)

    return max_subarray
