class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def partition(self, l, r):
        # obtain pivot
        pivot = self.nums[r]
        i = l
        for j in range(l, r):
            if self.nums[j] < pivot:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                # increase index of smaller elements
                i += 1
        self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return i

    def sort(self, l, r):
        if l >= r:
            return
        # top-down
        idx = self.partition(l, r)
        self.sort(l, idx - 1)
        self.sort(idx + 1, r)
