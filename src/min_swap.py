def min_swap(nums):
    n = len(nums)

    visited = [False] * n
    inverted_idx = {num: idx for idx, num in enumerate(sorted(nums))}

    num = 0
    for i in range(n):
        count = -1
        while not visited[i] and i != inverted_idx[nums[i]]:
            visited[i] = True
            i = inverted_idx[nums[i]]

            count += 1

        num += max(0, count)

    return num
