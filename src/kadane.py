def kadane(nums):
    max_subarray, curr_max = float("-INF"), 0
    for num in nums:
        curr_max = max(curr_max + num, num)
        max_subarray = max(max_subarray, curr_max)

    return max_subarray
