class NextPermutation:
    def __init__(self, nums):
        self.nums = nums

    def next(self):
        l = r = len(self.nums) - 1
        while l > 0 and self.nums[l-1] >= self.nums[l]:
            l -= 1
        if l == 0:
            # if it doesn't exist, return smallest
            self.nums.reverse()
        else:
            while self.nums[r] <= self.nums[l-1]:
                r -= 1
            # swap and reverse suffix elements
            self.nums[l-1], self.nums[r] = self.nums[r], self.nums[l-1]
            self.nums[l:] = self.nums[l:][::-1]
