class MergeSort:
    def __init__(self, nums):
        self.nums = nums
        # create temp array
        self.temp = [-1 for _ in range(len(nums))]

    def merge(self, l, mid, r):
        i, j = l, mid + 1
        k = l
        while i <= mid and j <= r:
            if self.nums[i] < self.nums[j]:
                self.temp[k] = self.nums[i]
                i += 1
            else:
                self.temp[k] = self.nums[j]
                j += 1
            k += 1
        # merge remaining elements
        while i <= mid:
            self.temp[k] = self.nums[i]
            i += 1
            k += 1
        while j <= r:
            self.temp[k] = self.nums[j]
            j += 1
            k += 1
        # copy back into nums
        self.nums[l:r+1] = self.temp[l:r+1]

    def sort(self, l, r):
        if l >= r:
            return
        # bottom-up
        mid = l + ((r - l) >> 1)
        self.sort(l, mid)
        self.sort(mid + 1, r)
        self.merge(l, mid, r)
