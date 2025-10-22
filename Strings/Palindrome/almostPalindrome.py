# Import regex module so we can preprocess strings by removing non-alphanumeric chars.
import re

# Helper: check whether the substring s[left..right] (inclusive) is a palindrome.
# We compare characters inward until pointers cross or a mismatch is found.
def matchSubstringForPalindrome(left:int, right:int, s:str) -> bool:
    # Continue while the left index does not surpass the right index.
    while left <= right:
        # If characters at the mirrored positions differ, it's not a palindrome.
        if s[right] != s[left]:
            # Return early when a mismatch is detected to avoid extra work.
            return False
        # Move the pointers inward for the next comparison.
        left += 1
        right -= 1
    # If all mirrored pairs matched, the substring is a palindrome.
    return True

# Main function: determine if `s` is an "almost palindrome".
# Definition used here: you can delete at most one character to make `s` a palindrome.
def isStringAnAlmostPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and normalize to lowercase for case-insensitive checks.
    processed_s = re.sub(r"[^A-Za-z0-9]+", "", s).lower()

    # Initialize two-pointer indices to compare characters from both ends.
    left, right = 0, len(processed_s) - 1

    # While the pointers haven't crossed, compare characters at the ends.
    while left <= right:
        # If a mismatch occurs, we have one chance to skip a character.
        if processed_s[left] != processed_s[right]:
            # Try skipping either the left or the right character; if either results in a palindrome,
            # the original string qualifies as an almost-palindrome.
            return matchSubstringForPalindrome(left+1, right, processed_s) or matchSubstringForPalindrome(left, right - 1, processed_s)
        # If characters matched, move both pointers inward and continue.
        left += 1
        right -= 1
    # If no mismatches were found, the (processed) string is already a palindrome.
    return True

# --- Example usage / quick checks ---
# Example 1: contains spaces and letters; tests preprocessing and logic.
s1 = "race a car"
# Print whether s1 can be made a palindrome by removing at most one character.
print(isStringAnAlmostPalindrome(s1))

# Example 2: close to palindrome with only one extra character; should typically return True.
s2 = "abccdba"
# Print result for s2.
print(isStringAnAlmostPalindrome(s2))

# Example 3: not fixable by removing only one character; tests negative case.
s3 = "abcdefdba"
# Print result for s3.
print(isStringAnAlmostPalindrome(s3))

# Example 4: empty string edge case; empty string is a palindrome by definition.
s4 = ""
# Print result (expected True).
print(isStringAnAlmostPalindrome(s4))

# Example 5: single-character edge case; always a palindrome.
s5 = "a"
# Print result (expected True).
print(isStringAnAlmostPalindrome(s5))

# Example 6: two-character string where removing one char yields a palindrome.
s6 = "ab"
# Print result for s6 (should be True because removing either char yields a single-char palindrome).
print(isStringAnAlmostPalindrome(s6))

# Time complexity: O(n) where n is the length of the processed string, since we do a single pass with two pointers.
# Space complexity: O(n) due to the storage needed for the processed string after removing non-alphanumeric characters.
