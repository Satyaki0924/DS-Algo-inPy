
# This function finds the maximum area of water that can be contained between two lines in the 'container' list.
# It uses an optimal two-pointer approach to reduce the number of checks.
def findMaxAreaForWaterInContainer(container:list[int]):
    # Initialize the variable to keep track of the maximum area found so far.
    max_area = 0
    # Get the number of lines (walls) in the container.
    n = len(container)
    # Set two pointers: one at the start (left_p) and one at the end (right_p) of the container.
    left_p = 0; right_p = n - 1
    # Continue until the two pointers meet.
    while left_p < right_p:
        # Get the height of the left wall.
        left_wall = container[left_p]
        # Get the height of the right wall.
        right_wall = container[right_p]
        # The width is the distance between the two walls.
        width = right_p - left_p
        # The height of water is limited by the shorter wall.
        height = min(left_wall, right_wall)
        # Calculate the area that can be contained between these two walls.
        area = width * height
        # Update max_area if we found a bigger area.
        max_area = max(max_area, area)
        # Move the pointer at the shorter wall inward, hoping to find a taller wall for a bigger area.
        if left_wall < right_wall:
            # Move left pointer to the right if left wall is shorter.
            left_p += 1
            # Continue to the next iteration of the loop.
            continue
        # Move right pointer to the left if right wall is shorter or equal.
        right_p -= 1
    # After checking all possibilities, return the largest area found.
    return max_area

# Example 1: Test the function with a sample container.
container1 = [7, 1, 2, 3, 9]
# Print the max area for container1: 28
print("Max water area in container 1: ", findMaxAreaForWaterInContainer(container1))

# Example 2: Test the function with another sample container.
container2 = [6, 9, 3, 4, 5, 8]
# Print the max area for container2: 32
print("Max water area in container 2: ", findMaxAreaForWaterInContainer(container2))