# This function finds the maximum area of water that can be contained between two lines in the 'container' list.
# It uses a brute force approach by checking all possible pairs of lines.
def findMaxAreaForWaterInContainer(container: list[int]):
    # Initialize the variable to keep track of the maximum area found so far.
    max_area = 0
    # Get the number of lines (walls) in the container.
    n = len(container)
    # Loop through each possible position for the left wall.
    for left_p in range(0, n):
        # For each left wall, loop through all possible positions for the right wall to its right.
        for right_p in range(left_p + 1, n):
            # Get the height of the left wall.
            left_wall = container[left_p]
            # Get the height of the right wall.
            right_wall = container[right_p]
            # The height of water is limited by the shorter wall.
            height = min(left_wall, right_wall)
            # The width is the distance between the two walls.
            width = right_p - left_p
            # Calculate the area that can be contained between these two walls.
            area = height * width
            # Update max_area if we found a bigger area.
            max_area = max(max_area, area)
    # After checking all pairs, return the largest area found.
    return max_area

# Example 1: Test the function with a sample container.
container1 = [7, 1, 2, 3, 9]
# Print the max area for container1: 28
print("Max water area in container 1: ", findMaxAreaForWaterInContainer(container1))

# Example 2: Test the function with another sample container.
container2 = [6, 9, 3, 4, 5, 8]
# Print the max area for container2: 32
print("Max water area in container 2: ", findMaxAreaForWaterInContainer(container2))