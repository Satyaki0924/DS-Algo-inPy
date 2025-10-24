
def countKDiffPairs(nums: list, k: int) -> int:
    seen = {}
    for num in nums:
        if seen.get(num) is None:
            seen[num] = 0
        seen[num] += 1
    pairs = 0
    if k == 0:
        for num in seen.keys():
            if seen[num] > 1:
                pairs += 1
    else:
        for num in seen.keys():
            target = num + k
            if target in seen:
                pairs += 1
    return pairs


arr = [3,1,4,1,5]; k = 2
print(countKDiffPairs(arr, k))
arr = [1,2,3,4,5]; k = 1
print(countKDiffPairs(arr, k))
arr = [1,3,1,5,4]; k = 0
print(countKDiffPairs(arr, k))
