
# Problem: Maximum Subarray (LeetCode 53)
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Use Kadane's algorithm to solve in O(n) time and O(1) extra space.
#
# Easy explanation with example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# The maximum subarray is [4,-1,2,1] with sum 6.
# Kadane's algorithm keeps a running sum of the current subarray (reset to 0 when negative)
# and tracks the maximum seen so far.


# Return the maximum sum of any contiguous subarray in nums using Kadane's algorithm.
def findMaxSubarraySum(nums: list) -> int:
    # Handle empty input: specification here returns 0 for empty list (preserve original behavior).
    if len(nums) <= 0:
        return 0
    # max_sum stores the best subarray sum found so far; start with first element to handle all-negative arrays.
    max_sum = nums[0]
    # subarray_sum is the running sum for the current candidate subarray.
    subarray_sum = 0
    # Iterate over each number, extending the current subarray or restarting it when it's harmful.
    for num in nums:
        # If current running sum is negative, discarding it and starting fresh is better than extending it.
        if subarray_sum < 0:
            subarray_sum = 0
        # Extend the current subarray by adding the current number.
        subarray_sum += num
        # Update the global maximum if the running sum is now higher.
        max_sum = max(max_sum, subarray_sum)
    # Return the largest subarray sum found.
    return max_sum


# --- Example usage ---
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Expect 6 (subarray [4,-1,2,1])
print(findMaxSubarraySum(nums))

# Time complexity: O(n) where n is the number of elements in nums (single pass).
# Space complexity: O(1) since we use only a fixed amount of extra space.