"""Utility functions to check palindromes using several approaches.
Each helper below focuses on a specific technique; small wrappers show example runs.
"""

# Regular expressions used to remove non-alphanumeric characters when preprocessing inputs.
import re


# Remove any character that isn't a letter or digit and lowercase the result.
# Lowercasing ensures comparisons are case-insensitive (e.g., 'A' == 'a').
# The regex [^A-Za-z0-9] matches any character that is NOT in the ranges A-Z, a-z, or 0-9.
# ^ inside the brackets negates the character class. This matches unwanted characters for removal.
def removeCharsExceptStringAndNum(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", s).lower()


# Method 1: create a reversed copy of the string and compare character-by-character.
# This is a straightforward approach useful for small inputs and demonstration.
# Time complexity: O(n), Space complexity: O(n)
def findPalindromeWithReversal(s: str) -> bool:
    # Length of the string to quickly handle trivial cases.
    n = len(s)
    # Strings of length 0 or 1 are palindromes by definition.
    if n <= 1:
        return True
    # Build the reversed string by iterating indices from end to start.
    s2 = ''.join([s[i] for i in range(n-1, -1, -1)])
    # Compare characters at the same positions in the original and reversed strings.
    for i in range(0, n):
        if s[i] != s2[i]:
            # A single mismatch means the string is not a palindrome.
            return False
    # If all positions matched, it's a palindrome.
    return True


# Method 2: compare characters by expanding from the middle outwards.
# Useful to illustrate center-based palindrome checks for even and odd lengths.
# Time complexity: O(n), Space complexity: O(1)
def findPalindromeWithMidPointers(s: str) -> bool:
    # Determine the length and handle trivial cases first.
    n = len(s)
    if n <= 1:
        return True
    # Initialize left and right pointers depending on even/odd length.
    left = None; right = None
    if n % 2 == 0:
        # For even length, left is the left-of-center index and right is left+1.
        left = int(n/2) - 1
        right = left + 1
    else:
        # For odd length, both pointers start at the middle index.
        left = int(n//2)
        right = left
    # Expand outward while pointers remain within bounds.
    # Note: right should be strictly less than n, not <= n, to index the string safely.
    while left >= 0 and right < n:
        if s[left] != s[right]:
            # Mismatch indicates the string is not a palindrome using this center.
            return False
        left -= 1
        right += 1
    # If expansion completes without mismatches, it's a palindrome.
    return True


# Method 3: classic two-pointer approach from the ends moving inward.
# This is the most common and efficient approach (O(n) time, O(1) space).
# Time complexity: O(n), Space complexity: O(1)
def findPalindromeWithEndPointers(s: str) -> bool:
    # Quick length check for trivial cases.
    n = len(s)
    if n <= 1:
        return True
    left = 0
    right = n - 1

    # Move both pointers towards the center, comparing characters.
    while left <= right:
        if s[left] != s[right]:
            # If any pair differs, it's not a palindrome.
            return False
        left += 1
        right -= 1
    return True


# Helper that runs all three methods on an input and prints results for quick comparison.
def runAllMethods(s: str) -> None:
    print("Input: ", s)
    # Preprocess the input to remove non-alphanumeric characters and lowercase it.
    s = removeCharsExceptStringAndNum(s)
    # Print the result of each palindrome-checking method.
    print("findPalindromeWithEndPointers: ", findPalindromeWithEndPointers(s))
    print("findPalindromeWithMidPointers: ", findPalindromeWithMidPointers(s))
    print("findPalindromeWithReversal: ", findPalindromeWithReversal(s))
    print("\n")


# Example inputs used to demonstrate and test the three methods.
s1 = "aabaa"
s2 = "aabbaa"
s3 = "abc"
s4 = ""
s5 = "A man, a plan, a canal: panama"

# Run the demonstration for each example.
runAllMethods(s1)
runAllMethods(s2)
runAllMethods(s3)
runAllMethods(s4)
runAllMethods(s5)
