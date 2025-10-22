# Define a function that searches for the first occurrence of `needle` in `haystack`.
# We return the starting index of the first match, or -1 if no match exists.
def findNeedle(haystack: str, needle: str) -> int:
    # Precompute the length of the needle so we can slide a fixed-size window over haystack.
    needle_len = len(needle)
    # Initialize the left index of the sliding window to 0 (start of the haystack).
    left = 0
    # Initialize the right index of the window based on the needle length (inclusive index).
    right = needle_len - 1
    # Slide the window until the right index goes past the haystack end.
    while right < len(haystack):
        # Extract the substring covered by the current window (left..right inclusive).
        # We use slicing with right+1 because Python slices are end-exclusive.
        word = haystack[left:right+1]
        # If the current window's substring equals the needle, we've found the first occurrence.
        if word == needle:
            # Return the left index where the needle starts in the haystack.
            return left
        # Move the sliding window one step to the right by incrementing left.
        left += 1
        # Move the right index correspondingly so the window size remains equal to needle_len.
        right += 1
    # If we finished sliding and never returned, the needle wasn't found; return -1 per convention.
    return -1

# --- Example usages below ---
# Example 1: haystack contains the needle; expected output is the starting index of the first match.
haystack1 = "sadbutsad"
needle1 = "sad"
# Print the index of the first occurrence of needle1 inside haystack1.
print(findNeedle(haystack1, needle1))

# Example 2: haystack does not contain the needle; expected output is -1.
haystack2 = "leetcode"
needle2 = "leeto"
# Print the result to verify correct handling when the needle is absent.
print(findNeedle(haystack2, needle2))

# Time complexity: O((N-L)*L) in the worst case, where N is the length of haystack and L is the length of needle.
# Space complexity: O(1) since we use only a fixed amount of extra space.