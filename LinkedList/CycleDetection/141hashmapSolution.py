# Import helper functions and Node type from the sibling Singly module.
# The relative import assumes this file sits under a package where '..Singly' resolves correctly.
from ..Singly import *

# Problem 141. Linked List Cycle Detection using Hash Map
# Detect whether a singly linked list contains a cycle using a hash map of visited nodes.
# This function returns True as soon as it sees a node for the second time.
def isLinkedListCylcic(head: Node) -> bool:
    # Use a dict as a visited set to store nodes we've seen during traversal.
    seen = {}
    # Walk the list following next pointers until we reach the end (None) or detect a cycle.
    while head != None:
        # If the current node is already in the seen map, we have a cycle.
        if seen.get(head) is not None:
            return True
        # Mark the current node as seen; stored value is unused (we use dict as a set).
        seen[head] = 0
        # Move to the next node in the list.
        head = head.next
    # If we finished traversal without repeats, there is no cycle.
    return False


# --- Example usage: build a cyclic list and check for a cycle ---
# values list describes node values; pos is index where tail connects (0-based) or -1 for no cycle.
values = [3,2,0,-4]; pos = 1
# Create a cyclic linked list using the helper from Singly (assumes helper supports pos parameter).
head = createCyclicLinkedList(values, pos)
# Print True/False depending on whether a cycle is detected.
print(isLinkedListCylcic(head))

# Time complexity: O(n) where n is the number of nodes until cycle detection or list end.
# Space complexity: O(n) for the hash map storing visited nodes in the worst case (no cycle).