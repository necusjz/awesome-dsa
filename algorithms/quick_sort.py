def quick_sort(nums):
    def partition(l, r):
        # set pivot
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                # increase index of smaller element
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def sort(l, r):
        if l >= r:
            return
        # top-down
        idx = partition(l, r)
        sort(l, idx - 1)
        sort(idx + 1, r)

    lo, hi = 0, len(nums) - 1
    sort(lo, hi)
