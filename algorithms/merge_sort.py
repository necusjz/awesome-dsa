def merge_sort(nums):
    def merge(l, mid, r):
        i, j = l, mid + 1
        k = l
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        # merge remaining elements
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= r:
            temp[k] = nums[j]
            j += 1
            k += 1
        # copy back into nums
        nums[l:r+1] = temp[l:r+1]

    def sort(l, r):
        if l >= r:
            return
        mid = l + ((r - l) >> 1)
        sort(l, mid)
        sort(mid + 1, r)
        # bottom-up
        merge(l, mid, r)

    lo, hi = 0, len(nums) - 1
    # initialize temp array (n)
    temp = [-1] * len(nums)
    sort(lo, hi)
