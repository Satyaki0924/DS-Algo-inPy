
"""Compare two typed-out strings where '#' represents a backspace.

We simulate typing both strings, applying backspaces, and then compare final outputs.
"""

# Define a function that returns True if final typed strings are equal.
def findOutIfStringMatches(S: str, T: str) -> bool:
    # Containers (lists) to build final characters after processing backspaces.
    final_S = []
    final_T = []

    # Process string S character by character.
    for char in S:
        # If current character is '#' it means backspace: remove last char if exists.
        if char == "#":
            # Only pop if there is something to remove. Else do nothing.
            if len(final_S) > 0:
                final_S.pop()
        else:
            # Otherwise append the character to the resulting list.
            final_S.append(char)

    # Process string T in the same way as S.
    for char in T:
        if char == "#":
            # Only pop if there is something to remove. Else do nothing.
            if len(final_T) > 0:
                final_T.pop()
        else:
            final_T.append(char)

    # Compare the final lists of characters for equality and return the result.
    return (final_S == final_T)

# Example testcases to demonstrate behaviour and edge cases.
s1 = "ab#z"
t1 = "az#z"
# Expected: True (both resolve to 'az')
print(findOutIfStringMatches(s1, t1))

s2 = "abc#d"
t2 = "acc#c"
# Expected: False
print(findOutIfStringMatches(s2, t2))

s3 = "x#y#z#"
t3 = "a#"
# Expected: True (both resolve to empty string)
print(findOutIfStringMatches(s3, t3))

s4 = "a###b"
t4 = "b"
# Expected: True (backspaces remove 'a', then 'b' remains)
print(findOutIfStringMatches(s4, t4))

s5 = "Ab#z"
t5 = "ab#z"
# Expected: False (case-sensitive)
print(findOutIfStringMatches(s5, t5))

s6 = "y#fo##f"
t6 = "y#f#o##f"
# Expected: True or False depending on correct processing (test demonstrates)
print(findOutIfStringMatches(s6, t6))

s7 = "a"
t7 = "aa#a"
# Expected: True (both result in 'a')
print(findOutIfStringMatches(s7, t7))

# Time complexity is O(M + N) where M and N are lengths of S and T respectively.
# Space complexity is O(M + N) in the worst case where no backspaces occur.