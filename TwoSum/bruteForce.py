# Function to find two numbers in 'arr' that add up to target 't'
def findPair(arr, t):
    # Get the length of the input array
    n = len(arr)
    # If there are fewer than 2 elements, no pair can be formed
    if n < 2:
        return None
    # Iterate through each element in the array
    for i in range(0, n):
        # Calculate the difference needed to reach target 't' with arr[i] (Pointer P1)
        diff = t - arr[i]
        # Check all elements from 1 element after current position of arr[i] with arr[j] (Pointer P2) to avoid using the same element twice
        for j in range(i+1, n):
            # If a matching pair is found, return their values and indices
            if arr[j] == diff:
                return {"items": [arr[i], arr[j]], "indices": [i, j]}
    # If no pair is found, return None
    return None

# Example usage: find a pair in the array that sums to 11
res = findPair([1, 3, 7, 9, 2], 11)
# Print the result (pair and their indices, or None)
print(res)
# Time complexity is O(N^2) due to nested loops
# Space complexity is O(1) as no extra space is used