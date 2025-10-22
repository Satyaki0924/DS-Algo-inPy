
# Define a function to compute the length of the longest substring without repeating characters.
# This function takes a string and returns an integer length; we use a brute-force expansion from each start.
def findLongestSubstring(string: str) -> int:
    # Initialize the maximum substring length found so far to zero.
    # Keeping this variable lets us compare all candidate substrings and return the best.
    max_length = 0
    # Store the length of the input string once to avoid recomputing len(string) repeatedly in loops.
    n = len(string)
    # Iterate over every possible starting index i for a substring (0..n-1).
    # For each start, we'll try to expand the substring until a duplicate character is found.
    for i in range(0, n):
        # Reset the length counter for the current start; it counts unique characters from i.
        length = 0
        # Use a dictionary as a set to track characters we've seen in the current substring.
        # We use a dict because it allows O(1) membership checks with .get().
        seen = {}
        # Expand the substring from j = i to the end of the string.
        # We stop early when a repeated character is encountered.
        for j in range(i, n):
            # Current character at position j that we want to include in the substring.
            curr_char = string[j]
            # If the current character has already been seen in this substring, we must stop.
            # Using seen.get(curr_char) allows us to check membership safely (returns None if absent).
            if seen.get(curr_char) is not None:
                # Break out of the inner loop because adding curr_char would violate uniqueness.
                break
            # Mark the current character as seen. The stored value is unused; dict functions as a set.
            seen[curr_char] = 0
            # Increment the current substring length since curr_char was unique so far.
            length += 1
        # After exploring substrings starting at i, update the overall maximum if needed.
        max_length = max(length, max_length)
    # Return the largest length found across all starting positions.
    return max_length

# --- Example usages below ---
# Example 1: a string with some repeated characters; expected output helps verify correctness.
s1 = "abccabb"
# Print the computed longest-unique-character substring length for s1.
print(findLongestSubstring(s1))

# Example 2: a string where every character is the same; longest unique substring is length 1.
s2 = "ccccccc"
# Print the result for s2 to confirm function handles repeated characters correctly.
print(findLongestSubstring(s2))

# Example 3: empty string edge case; expected result is 0 because there are no characters.
s3 = ""
# Print the result for the empty string to verify edge-case handling.
print(findLongestSubstring(s3))

# Example 4: mixed characters with duplicates; another test to validate behavior.
s4 = "abcbda"
# Print the computed result for s4 as a final example.
print(findLongestSubstring(s4))

# Time complexity: O(n^2) in the worst case, where n is the length of the input string.
# Space complexity: O(min(m, n)), where m is the size of the character set and n is the length of the string.