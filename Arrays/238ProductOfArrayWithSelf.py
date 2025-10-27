# Problem: Product of Array Except Self (LeetCode 238)
# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i]. Solve it without using division and in O(n) time.
#
# Explanation (easy): compute the product of all elements to the left of each index (prefix)
# and the product of all elements to the right of each index (postfix). Multiply them to get
# the final value for each index. We compute prefix in a left-to-right pass and multiply by
# postfix in a right-to-left pass, storing the result in a single output array.
#
# Example:
# nums = [1,2,3,4]
# prefix products (at each index i, product of elements left of i): [1, 1, 2, 6]
# postfix products (product of elements right of i): [24, 12, 4, 1]
# result (elementwise product): [24, 12, 8, 6]


# Compute product of array except self without division.
def productExceptSelf(nums: list) -> list:
    # n is the number of elements in the input list.
    n = len(nums)
    # Initialize result array with zeros; we'll fill it with prefix products then scale by postfix.
    result = [0 for i in range(n)]
    # --- Prefix pass ---
    # prefix holds the running product of elements left of the current index.
    # For the first index, there are no elements to the left, so prefix starts at 1.
    prefix = 1
    # Iterate left-to-right storing the prefix product at each position.
    for i in range(n):
        # Store the product of all elements to the left of i.
        result[i] = prefix
        # Update prefix by multiplying with current element so next index sees it.
        prefix *= nums[i]

    # --- Postfix pass ---
    # postfix holds the running product of elements right of the current index.
    # Start with 1 for the last index (no elements to the right).
    postfix = 1
    # Iterate right-to-left, multiply the stored prefix by the postfix to get final result.
    for i in range(n-1, -1, -1):
        # Multiply stored prefix by current postfix to incorporate right-side products.
        result[i] *= postfix
        # Update postfix to include current element for the next iteration to the left.
        postfix *= nums[i]

    # Return the array where each position i has product of all elements except nums[i].
    return result


# --- Example usage ---
nums = [1,2,3,4]
# Expect [24, 12, 8, 6]
print(productExceptSelf(nums))

# Time complexity: O(n) where n is the number of elements in nums (two passes through the list).
# Space complexity: O(1) if we don't count the output array (we use only a fixed number of extra variables).