
"""LeetCode 209 - Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`,
find the minimal length of a contiguous subarray of which the sum is at least
`target`. If there is no such subarray, return 0.

This implementation uses the sliding-window (two-pointer) technique:
- Expand the right end to increase the window sum.
- When the sum >= target, shrink from the left to try to minimize window size.

Example:
    nums = [2,3,1,2,4,3], target = 7 -> minimal window length = 2  (subarray [4,3])

Time complexity: O(n) — each element visited at most twice.
Space complexity: O(1).
"""

# Define the function that finds the minimal-length subarray with sum >= target.
def findSubArrayWithMinSum(nums: list, target: int) -> int:
    # `left` is the start index of our sliding window.
    left = 0
    # `sum` will hold the current window sum (note: shadows built-in `sum`, kept for parity with original code).
    sum = 0
    # `min_window` will track the smallest window length found; None means not found yet.
    min_window = None

    # Expand the window by moving `right` from 0..len(nums)-1.
    for right in range(len(nums)):
        # `curr` is the value at the right end which we'll add to the window sum.
        curr = nums[right]
        # Add current element to the running window sum.
        sum += curr
        # While current window sum meets or exceeds target, try to shrink from left.
        while sum >= target:
            # Current window length from left to right inclusive.
            window = right - left + 1
            # If we haven't set min_window yet, initialize it with current window.
            if min_window is None:
                min_window = window
            # Otherwise update min_window with the smaller of current and previous.
            min_window = min(window, min_window)

            # Prepare to shrink the window: remove the leftmost element from sum.
            left_num = nums[left]
            sum -= left_num
            # Move left pointer right by one to reduce window size.
            left += 1
    # If no valid window was found, return 0 to indicate failure per problem statement.
    if min_window == None:
        return 0
    # Otherwise return the smallest window length found.
    return min_window


# Quick example run from the problem statement to verify behavior.
target = 7; nums = [2,3,1,2,4,3]
print(findSubArrayWithMinSum(nums, target))

# Time complexity: O(n) where n is the length of nums (each element processed at most twice).
# Space complexity: O(1) since we use only a fixed amount of extra space.