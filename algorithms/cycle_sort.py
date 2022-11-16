def min_swap(nums):
    ret = 0
    n = len(nums)
    visited = [False] * n
    inverted_idx = {num: idx for idx, num in enumerate(sorted(nums))}

    for idx in range(n):
        count = -1
        while not visited[idx] and idx != inverted_idx[nums[idx]]:
            visited[idx] = True
            idx = inverted_idx[nums[idx]]
            count += 1
        ret += max(0, count)

    return ret
