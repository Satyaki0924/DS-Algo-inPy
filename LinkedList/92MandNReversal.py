# Import helper functions and Node definition for singly-linked lists from the project's Singly module.
from Singly import *


# Reverse the nodes of a linked list from position left to position right (1-indexed).
# This mirrors LeetCode 92: reverse a sublist in-place and return the head of the modified list.
def swapMandNNodes(head: Node, left: int, right: int):
    # If left == right or list is empty, no changes are required; return the original head.
    if left == right or not head:
        return head
    
    # Use a dummy node to simplify edge cases (e.g., reversing from head position).
    dummy = Node(0)
    dummy.next = head

    # Initialize pointers: beforeLeft points to node before the left position,
    # afterRight will point to the node after the reversed segment, pos tracks position.
    beforeLeft, afterRight, pos = dummy, None, 1

    # Start traversal from the real head.
    curr = head

    # Move curr forward until it reaches the left position; keep beforeLeft behind it.
    while (pos < left and curr != None):
        beforeLeft = curr
        curr = curr.next
        pos += 1
    
    # tailOfReverse will become the tail of the reversed segment after operation.
    tailOfReverse = curr
    # headOfReverse will be the head of the reversed segment as we build it.
    headOfReverse = None

    # Reverse nodes from left to right by standard iterative link-reversal technique.
    while (left <= pos and pos <= right and curr != None):
        # Take current node out and prepend it to the reversed segment.
        temp = curr
        # Advance curr so we don't lose the remainder of the list.
        curr = curr.next
        # Point extracted node to current head of reversed segment.
        temp.next = headOfReverse
        # Move headOfReverse to point to the newly added node.
        headOfReverse = temp

        # afterRight tracks the node immediately following the reversed region.
        afterRight = curr
        pos += 1
    
    # Reconnect the node before the reversed region to the new head of the reversed segment.
    beforeLeft.next = headOfReverse
    # Connect the original left-node (now tailOfReverse) to the node after the reversed region.
    tailOfReverse.next = afterRight

    # Return the new list head (skip dummy).
    return dummy.next


# --- Example 1: very small list (edge case) ---
values = [3,5]
# Reverse the entire list from position m to n
m = 1
n = 2
# Build linked list using helper function
head = createLinkedList(values)

# Print original list for demonstration
print("Original LinkedList")
printLinkedList(head)

# Reverse the sublist and print the result
print("M & N reversed LinkedList")
head = swapMandNNodes(head, m, n)
printLinkedList(head)


# --- Example 2: larger list, reverse a middle segment ---
values = [1,3,5,7,9,11,13,15]
m = 3
n = 6
head = createLinkedList(values)

print("Original LinkedList")
printLinkedList(head)

print("M & N reversed LinkedList")
head = swapMandNNodes(head, m, n)
printLinkedList(head)

# Time complexity: O(n) where n is the number of nodes in the list (we may traverse the entire list).
# Space complexity: O(1) additional space since we only use a few pointers regardless of list size.