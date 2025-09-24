# This function solves the Two Sum problem efficiently using a dictionary (hash map).
# The goal: Find two numbers in 'arr' that add up to 't'.
# Instead of checking every possible pair (which is slow and O(N^2)),
# we use a dictionary to remember what number we need to complete the sum for each element.
def findPair(arr, t):
    # 'n' is the length of the array. We need this to loop through all elements.
    n = len(arr)
    # 'seen' will store numbers we need to find, mapped to the index where we need them.
    # For example, if we see a number x, and need (t-x) to complete the sum,
    # we store: seen[t-x] = index of x
    seen = {}
    # Loop through each number in the array, one by one.
    for i in range(0, n):
        # If the current number is in 'seen', it means we've already seen a number
        # that needs this number to complete the sum. So, we've found our pair!
        if seen.get(arr[i]):
            # We return both the numbers and their indices.
            return {"items": [arr[i], t-arr[i]], "indices": [seen[arr[i]], i]}
        # Otherwise, calculate what number we need to find in the future to complete the sum with arr[i].
        # For example, if arr[i] is 3 and t is 11, we need 8 (because 3 + 8 = 11).
        diff = t - arr[i]
        # Store this needed number in 'seen', with the current index.
        # If we see this needed number later in the array, we'll know we've found a pair.
        seen[diff] = i

# Let's test our function with an example array and target sum.
res = findPair([1, 3, 7, 9, 2], 11)
# Print the result. It will show the pair of numbers and their indices if found, or None if not found.
print(res)
# This solution is much faster than checking every possible pair.
# Time complexity: O(N) because we only loop through the array once.
# Space complexity: O(N) because we may store up to 'n' needed numbers in the dictionary.