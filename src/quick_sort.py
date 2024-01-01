import random


def quick_sort(nums):
    def partition(l, r):
        idx = random.randint(l, r)
        nums[idx], nums[r] = nums[r], nums[idx]
        pivot = nums[r]  # set pivot

        i = l
        for j in range(l, r):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1  # increase index of smaller

        nums[i], nums[r] = nums[r], nums[i]

        return i

    def sort(l, r):
        if l >= r:
            return

        idx = partition(l, r)  # top-down

        sort(l, idx - 1)
        sort(idx + 1, r)

    lo, hi = 0, len(nums) - 1

    sort(lo, hi)
