def next_permutation(nums):
    l = r = len(nums) - 1
    while l > 0 and nums[l] <= nums[l-1]:
        l -= 1

    if l == 0:
        return nums[::-1]  # smallest instead

    while nums[r] <= nums[l-1]:
        r -= 1

    # swap and reverse suffix
    nums[l-1], nums[r] = nums[r], nums[l-1]
    nums[l:] = nums[l:][::-1]

    return nums
