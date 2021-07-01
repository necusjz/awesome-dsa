def heap_sort(nums):
    def heapify(n, i):
        # find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and nums[i] < nums[l]:
            largest = l
        if r < n and nums[largest] < nums[r]:
            largest = r
        if largest != i:
            # swap root and largest, continue heapify
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    n = len(nums)
    # build max heap (n)
    for idx in range(n // 2 - 1, -1, -1):
        heapify(n, idx)
    # heap sort (nlogn)
    for idx in range(n - 1, 0, -1):
        nums[idx], nums[0] = nums[0], nums[idx]
        heapify(idx, 0)
