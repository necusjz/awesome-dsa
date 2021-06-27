def next_permutation(nums):
    l = r = len(nums) - 1
    while l > 0 and nums[l-1] >= nums[l]:
        l -= 1
    if l == 0:
        # if it doesn't exist, return smallest
        nums = nums[::-1]
        return nums
    while nums[r] <= nums[l-1]:
        r -= 1
    # swap and reverse suffix elements
    nums[l-1], nums[r] = nums[r], nums[l-1]
    nums[l:] = nums[l:][::-1]
    return nums
