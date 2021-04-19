class HeapSort:
    def __init__(self, nums):
        self.nums = nums

    def heapify(self, n, i):
        # find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.nums[i] < self.nums[l]:
            largest = l
        if r < n and self.nums[largest] < self.nums[r]:
            largest = r
        # swap root and largest, continue heapify
        if largest != i:
            self.nums[i], self.nums[largest] = self.nums[largest], self.nums[i]
            self.heapify(n, largest)

    def sort(self):
        n = len(self.nums)
        # build max heap (n)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        # heap sort (nlogn)
        for i in range(n - 1, 0, -1):
            self.nums[i], self.nums[0] = self.nums[0], self.nums[i]
            self.heapify(i, 0)
