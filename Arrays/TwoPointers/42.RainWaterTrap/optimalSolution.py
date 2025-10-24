
"""Optimal O(n) solution to the trapping rain water problem using two pointers.

We maintain two pointers (left and right) and track the maximum wall seen so far
from each side. At each step we move the pointer with the smaller current height
and accumulate water based on the trapped depth relative to that side's max.
"""

# Define the function that computes trapped water from an elevation map 'container'.
def calculateTrappedRainWater(container):
    # Number of bars in the elevation map.
    n = len(container)
    # Accumulates the total trapped water.
    total_water = 0
    # Initialize two pointers at both ends and variables to track left/right maxima.
    left_p = 0; right_p = n - 1; left_block_max = 0; right_block_max = 0;

    # Process until the two pointers meet.
    while left_p < right_p:
        # Heights at the current left and right pointers.
        curr_left_block = container[left_p]
        curr_right_block = container[right_p]

        # Always advance the side with the smaller height because the trapped
        # water is limited by the smaller boundary.
        if curr_left_block < curr_right_block:
            # If current left block is a new maximum, update left_block_max. This step avoids any negative number in sum.
            # if a new max is found, and we perform left_block_max(old max) - curr_left_block(new max), answer would be negative which would be wrong. Water level cannot be in negative.
            if curr_left_block >= left_block_max:
                left_block_max = curr_left_block
            else:
                # Otherwise, water can be trapped above the current left block.
                total_water += (left_block_max - curr_left_block)
            # Move left pointer inward to continue scanning.
            left_p += 1
        else:
            # If current right block is a new maximum, update right_block_max.
            if curr_right_block >= right_block_max:
                right_block_max = curr_right_block
            else:
                # Otherwise, water can be trapped above the current right block.
                total_water += (right_block_max - curr_right_block)
            # Move right pointer inward to continue scanning.
            right_p -= 1

    # After the loop, total_water holds the total trapped rainwater.
    return total_water

# Example 1: test array with multiple pockets of trapped water.
arr1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
# Print the computed trapped water for arr1.
print(calculateTrappedRainWater(arr1))

# Example 2: small test where the middle block is higher, so no water above it.
arr2 = [3, 4, 3]
# Print the computed trapped water for arr2.
print(calculateTrappedRainWater(arr2))

# Time complexity is O(N) since we traverse the list at most once.
# Space complexity is O(1) as we use only a fixed amount of extra space.
