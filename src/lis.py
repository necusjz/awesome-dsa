from bisect import bisect_left


def longest_increasing_subsequence(nums):
    lis = []
    for num in nums:
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            idx = bisect_left(lis, num)
            lis[idx] = num

    return len(lis)
