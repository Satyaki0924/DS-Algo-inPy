
# Define a function that returns the length of the longest substring without repeating characters.
# This version uses the optimal sliding-window approach with two pointers.
def findLongestSubstring(string: str) -> int:
    # Track the maximum length seen so far across all windows.
    max_length = 0
    # The left side of the sliding window. We will move this forward when duplicates are found.
    left_pointer = 0
    # A dictionary mapping characters to their most recent index in the string.
    # This lets us quickly determine if a character inside the current window repeats.
    seen = {}
    # Expand the right side of the window over every index in the string.
    for right_pointer in range(0, len(string)):
        # Character at the right pointer that we want to include in the window.
        curr_char = string[right_pointer]
        # If the character was seen before, we may need to move the left pointer.
        # Using seen.get avoids KeyError and returns None if unseen.
        if seen.get(curr_char) is not None:
            # Retrieve the previous index where curr_char was seen.
            prev_char = seen[curr_char]
            # Only move left_pointer if the previous occurrence is inside the current window.
            # This check ensures left_pointer never moves backwards.
            if prev_char >= left_pointer:
                # Move left_pointer to the position right after the previous occurrence.
                left_pointer = prev_char + 1
        # Update the most recent index for curr_char to the current right_pointer.
        seen[curr_char] = right_pointer
        # Update the maximum window length: window size is (right_pointer - left_pointer + 1).
        max_length = max(max_length, (right_pointer - left_pointer) + 1)
    # After scanning the string, return the largest unique-character substring length found.
    return max_length


# --- Example usages below ---
# Example 1: mixed characters with repeats; useful to verify correctness.
s1 = "abccabb"
# Print result for s1 to validate the algorithm.
print(findLongestSubstring(s1))

# Example 2: all characters identical; expected longest unique substring length is 1.
s2 = "ccccccc"
# Print result for s2 to validate handling of repeated characters.
print(findLongestSubstring(s2))

# Example 3: empty string edge case; expected result is 0.
s3 = ""
# Print result for the empty string to confirm edge-case handling.
print(findLongestSubstring(s3))

# Example 4: another mixed example to exercise the sliding window movement.
s4 = "abcbda"
# Print the computed result for s4 as a final example.
print(findLongestSubstring(s4))

# Time complexity: O(n) in the worst case, where n is the length of the input string.
# Space complexity: O(min(m, n)), where m is the size of the character set and n is the length of the string.