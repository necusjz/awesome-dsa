def heap_sort(nums):
    def heapify(n, i):
        largest = i
        l, r = i * 2 + 1, i * 2 + 2

        # find largest among parent and its children
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r

        if largest != i:  # swap parent and largest child, continue heapify
            nums[largest], nums[i] = nums[i], nums[largest]
            heapify(n, largest)

    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):  # build max heap, O(n)
        heapify(n, i)

    for i in range(n - 1, 0, -1):  # heap sort, O(nlogn)
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
