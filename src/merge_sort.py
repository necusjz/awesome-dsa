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

        # merge remaining
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= r:
            temp[k] = nums[j]
            j += 1
            k += 1

        nums[l:r+1] = temp[l:r+1]  # copy back

    def sort(l, r):
        if l >= r:
            return

        mid = l + ((r - l) >> 1)
        sort(l, mid)
        sort(mid + 1, r)

        merge(l, mid, r)  # bottom-up

    lo, hi = 0, len(nums) - 1
    temp = [None] * len(nums)  # initialize temp array, O(n)

    sort(lo, hi)
