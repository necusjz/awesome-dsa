class NextPermutation:
    def __init__(self, nums):
        self.nums = nums

    def next(self):
        p1 = p2 = len(self.nums) - 1
        while p1 > 0 and self.nums[p1-1] >= self.nums[p1]:
            p1 -= 1
        if p1 == 0:
            # if it doesn't exist, return smallest
            self.nums.reverse()
        else:
            while self.nums[p2] <= self.nums[p1-1]:
                p2 -= 1
            # swap and reverse suffix elements
            self.nums[p1-1], self.nums[p2] = self.nums[p2], self.nums[p1-1]
            self.nums[p1:] = self.nums[p1:][::-1]
