def findPair(arr, t):
    n = len(arr)
    if n < 2:
        return None
    for i in range(0, n):
        diff = t - arr[i]
        for j in range(i, n):
            if arr[j] == diff:
                return {"items": [arr[i], arr[j]], "idx": [i, j]}
    return None

res = findPair([1, 3, 7, 9, 2], 11)
print(res)
# O (N)