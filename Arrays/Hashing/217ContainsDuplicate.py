
# Problem: Contains Duplicate (LeetCode 217)
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Goal: Implement an O(n) time, O(n) space solution using a hash set/map.


# Check whether the input list contains any duplicate elements.
# Input: nums - list of integers. Output: True if a duplicate exists, otherwise False.
def containsDuplicates(nums: list) -> bool:
    # Use a dictionary as a set to record values we've seen while iterating.
    seen = {}
    # Iterate through each number in the list once (O(n) time).
    for num in nums:
        # If the number is already recorded in seen, we found a duplicate.
        if seen.get(num) is not None:
            return True
        # Otherwise mark this number as seen; stored value is unused (dict used as set).
        seen[num] = 0
    # If we finished the loop without finding duplicates, return False.
    return False


# --- Example usage ---
# Example input contains duplicate '1', so expected output is True.
nums = [1,2,3,1]
# Print the result of the duplicate check for the example input.
print(containsDuplicates(nums))

# Time complexity: O(n) where n is the number of elements in nums (we do a single pass).
# Space complexity: O(n) in the worst case where all elements are unique (we store them all).