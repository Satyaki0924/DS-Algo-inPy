
"""Optimal backward-scan solution for comparing typed-out strings with '#' as backspace.

We scan both strings from the end toward the start. When we encounter '#',
we skip the appropriate number of characters (simulating backspace) and only
compare visible characters. This avoids extra memory allocation.
"""

# Define the function implementing the backward two-pointer strategy.
def findOutIfStringMatches(S: str, T: str) -> bool:
    # Lengths of S and T.
    len_s = len(S); len_t = len(T)
    # Start pointers at the end of each string.
    s_pointer = len_s - 1; t_pointer = len_t - 1
    # Continue until both pointers have scanned past the start.
    while s_pointer >= 0 or t_pointer >= 0:
        # Get current characters if pointers are valid, else None.
        # Because Python allows negative indices, we guard against pointer < 0.
        s_char = S[s_pointer] if s_pointer >= 0 else None
        t_char = T[t_pointer] if t_pointer >= 0 else None

        # If either side has a backspace marker, skip characters accordingly.
        if s_char == "#" or t_char == "#":
            # Handle backspaces on the S side.
            if s_char == "#":
                # backcounter counts how many steps to skip (1 for the '#', 1 for the char to remove)
                backcounter = 2
                # Move the S pointer left backcounter steps, but if we encounter
                # nested '#' we extend the count (each '#' causes two more steps).
                while backcounter > 0 and s_pointer >= 0:
                    s_pointer -= 1
                    backcounter -= 1
                    prev_s_char = S[s_pointer] if s_pointer >= 0 else None
                    if prev_s_char == "#":
                        backcounter += 2
            # Handle backspaces on the T side.
            if t_char == "#":
                backcounter = 2
                while backcounter > 0 and t_pointer >= 0:
                    t_pointer -= 1
                    backcounter -= 1
                    prev_t_char = T[t_pointer] if t_pointer >= 0 else None
                    if prev_t_char == "#":
                        backcounter += 2
        else:
            # If both current visible characters exist and are different, not equal.
            if s_char != t_char:
                return False

            # Move both pointers left to continue comparing previous characters.
            s_pointer -= 1
            t_pointer -= 1

    # If we finished scanning without mismatches, strings match.
    return True

# Example testcases to verify the algorithm.
s1 = "ab#z"
t1 = "az#z"
print(findOutIfStringMatches(s1, t1))

s2 = "abc#d"
t2 = "acc#c"
print(findOutIfStringMatches(s2, t2))

s3 = "x#y#z#"
t3 = "a#"
print(findOutIfStringMatches(s3, t3))

s4 = "a###b"
t4 = "b"
print(findOutIfStringMatches(s4, t4))

s5 = "Ab#z"
t5 = "ab#z"
print(findOutIfStringMatches(s5, t5))

s6 = "y#fo##f"
t6 = "y#f#o##f"
print(findOutIfStringMatches(s6, t6))

s7 = "a"
t7 = "aa#a"
print(findOutIfStringMatches(s7, t7))

# Time complexity is O(M + N) where M and N are lengths of S and T respectively.
# Space complexity is O(1) as we use only a fixed amount of extra space.