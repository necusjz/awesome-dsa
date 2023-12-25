def heap_sort(nums):
    def heapify(n, i):
        largest = i
        l, r = i * 2 + 1, i * 2 + 2
        # find largest among root and children
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r

        # swap root and largest, continue heapify
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            heapify(n, largest)

    n = len(nums)
    # build max heap, O(n)
    for idx in range(n // 2 - 1, -1, -1):
        heapify(n, idx)

    # heap sort, O(nlogn)
    for idx in range(n - 1, 0, -1):
        nums[idx], nums[0] = nums[0], nums[idx]
        heapify(idx, 0)
