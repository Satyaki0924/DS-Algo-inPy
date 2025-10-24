# This function solves the Two Sum problem efficiently using a dictionary (hash map).
# The goal: Find two numbers in 'arr' that add up to 't'.
# Instead of checking every possible pair (which is slow and O(N^2)),
# we use a dictionary to remember what number we need to complete the sum for each element.
def findPair(arr, t):
    # Get the length of the array so we can loop through all elements.
    n = len(arr)
    # If there are fewer than 2 elements, no pair can be formed
    if n < 2:
        return None
    # Create an empty dictionary to keep track of numbers we need to find, and the index where we need them.
    # For example, if we see a number x, and need (t-x) to complete the sum,
    # we store: seen[t-x] = index of x
    seen = {}
    # Loop through each number in the array, one by one.
    for i in range(0, n):
        # Store the current number for clarity.
        current_number = arr[i]
        # Check if the current number is in 'seen'.
        # If it is, we've already seen a number that needs this one to complete the sum.
        # That means we've found our pair!
        if seen.get(current_number):
            # Return the pair of numbers and their indices.
            return {"items": [t-current_number, current_number], "indices": [seen[current_number], i]}
        # Otherwise, calculate what number we need to find in the future to complete the sum with arr[i].
        # For example, if arr[i] is 3 and t is 11, we need 8 (because 3 + 8 = 11).
        diff = t - arr[i]
        # Store this needed number in 'seen', with the current index.
        # If we see this needed number later in the array, we'll know we've found a pair.
        seen[diff] = i
    # If we finish the loop without finding a pair, return None.
    return None

# Test our function with an example array and target sum.
res = findPair([1, 3, 7, 9, 2], 25)
# Print the result. It will show the pair of numbers and their indices if found, or None if not found.
print(res)
# This solution is much faster than checking every possible pair.
# Time complexity: O(N) because we only loop through the array once.
# Space complexity: O(N) because we may store up to 'n' needed numbers in the dictionary.