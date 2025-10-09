"""Optimal Two Sum solution for a sorted array using two pointers.

We move two pointers inward based on the current sum:
 - If sum < target -> move left pointer right to increase sum.
 - If sum > target -> move right pointer left to decrease sum.
 - If sum == target -> we found the pair.
"""

# Define a function to find the indices of two numbers that add up to 'target'.
def findIndices(numbers: list[int], target: int) -> list[int, int]:
    # Get the number of elements in the sorted list.
    n = len(numbers)
    # Initialize left pointer at the start and right pointer at the end.
    left = 0; right = n - 1
    # Loop while left pointer is to the left of right pointer.
    while left < right:
        # Read the values at both pointers (current candidates).
        left_num = numbers[left]
        right_num = numbers[right]
        # Calculate the sum of the two candidate numbers.
        curr_sum = left_num + right_num
        # If the sum matches the target, return the pair of indices.
        if curr_sum == target:
            return [left, right]
        # If the sum is too small, move the left pointer right to increase the sum.
        elif curr_sum < target:
            left += 1
        # If the sum is too large, move the right pointer left to decrease the sum.
        else:
            right -= 1
    # If no pair was found, return None to indicate that.
    return None

# Example input: sorted array of numbers.
numbers = [2, 5, 7, 9, 11, 15, 18, 22]
# Target sum we want to find from two numbers in the array.
target = 18
# Call the function and print the result (indices of the pair or None).
print(findIndices(numbers, target))

# Time complexity is O(N) because we traverse the list at most once.
# Space complexity is O(1) as we use only a fixed amount of extra space.
