# Problem: Linked List Cycle II (LeetCode 142)
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return -1.
# For this repository we return the 0-based index (position) where the cycle starts, or -1 when no cycle.
#
# Easy explanation (Floyd's algorithm) with example:
# - Example: values = [3,2,0,-4], pos = 1 means a list 3 -> 2 -> 0 -> -4 -> (back to node at index 1)
#   The cycle starts at value 2 (index 1). The function should return 1.
# - Floyd's idea: use two pointers (slow, fast). If they meet, a cycle exists.
#   To find the cycle start, reset one pointer to head and move both one step at a time;
#   the point where they meet is the cycle start.

# Import helpers and Node definition from the project's Singly list module.
from ..Singly import *


# Return the starting index (0-based) of the cycle in a linked list, or -1 if no cycle.
def isLinkedListCylcic(head: Node) -> int:
    # Initialize both pointers to the head of the list.
    fast, slow = head, head
    # Default return value when no cycle is found.
    pos = -1
    # If list is empty or has a single node with no next, it can't have a cycle.
    if fast == None or fast.next == None:
        return pos
    # Move fast and slow until they meet or fast reaches the end (no cycle).
    while True:
        # Advance slow by one step.
        fast = fast.next
        slow = slow.next
        # If fast reached the end, there's no cycle.
        if fast == None or fast.next == None:
            return pos
        # Advance fast a second step (fast moves two steps per loop; slow moves one).
        fast = fast.next
        # If pointers meet, we detected a cycle; break to find the entry point.
        if fast == slow:
            break
    # At this point, a cycle exists. To find entry position, reset a pointer to head.
    pos = 0
    # p1 starts from head, p2 starts from meeting point (fast == slow).
    p1 = head; p2 = fast
    # Move both pointers one step at a time; their meeting point is the cycle start.
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
        pos += 1
    # Return the index (0-based) where the cycle begins.
    return pos


# --- Example usage ---
# Example list: 3 -> 2 -> 0 -> -4 -> (back to index 1). Expected cycle start index: 1.
values = [3,2,0,-4]; pos = 1
# Build a cyclic linked list using helper (pos indicates 0-based index to link tail to, or -1 for none).
head = createCyclicLinkedList(values, pos)

# Print the computed start index of the cycle (1 for this example).
print(isLinkedListCylcic(head))

# Time complexity: O(n) where n is number of nodes until cycle detection or list end.
# Space complexity: O(1) since we only use a fixed number of pointers regardless of list size.