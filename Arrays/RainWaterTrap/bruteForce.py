
# Function to calculate trapped rain water using a brute-force approach.
def calculateTrappedRainWater(container):
    # Number of blocks in the elevation map.
    n = len(container)
    # Accumulator for total trapped water.
    total_water = 0
    # Track the maximum height seen to the left of the current position.
    max_left_block = 0
    # If there are fewer than 2 blocks, no water can be trapped.
    if n < 2:
        return total_water
    # Iterate over each position where water could be trapped (skip index 0).
    for pointer in range(1, n):
        # For every pointer, we'll compute the highest block to the right.
        max_right_block = 0
        # Look at the immediate left block to update left maximum.
        left_block = container[pointer - 1]
        # Update the maximum left block seen so far.
        max_left_block = max(max_left_block, left_block)
        # If we are at the last index or beyond, there is no room on the right.
        if pointer >= n-1:
            break
        # Scan to the right of the current pointer to find the highest block on the right.
        for right_pointer in range(pointer+1, n):
            # Height of the block at right_pointer.
            right_block = container[right_pointer]
            # Keep track of the maximum block to the right.
            max_right_block = max(max_right_block, right_block)
        # Current block height at the pointer position.
        current_height = container[pointer]
        # Water level above current block is limited by the smaller of max left/right.
        sum = min(max_left_block, max_right_block) - current_height
        # Only add positive trapped water (no negative contribution).
        if sum >= 0:
            total_water += sum
    # Return the total trapped water after scanning all positions.
    return total_water

# Example 1: an elevation map where multiple pockets of water exist.
arr1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
# Print the total amount of trapped water for arr1.
print(calculateTrappedRainWater(arr1))

# Example 2: a simple elevation map where water can be trapped between two taller blocks.
arr2 = [3, 4, 3]
# Print the trapped water for arr2 (should be 0 since the middle block is higher).
print(calculateTrappedRainWater(arr2))

# Time complexity is O(N^2) due to the nested loops scanning left and right for each position.
# Space complexity is O(1) as we use only a fixed amount of extra space.

