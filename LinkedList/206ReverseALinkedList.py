# Problem: Reverse a singly linked list (LeetCode 206)
# Given the head of a singly linked list, reverse the list, and return the reversed list's head.
# Example: Input: 1 -> 3 -> 5 -> 7 -> 9  -> Output: 9 -> 7 -> 5 -> 3 -> 1
# Constraints/Notes: This should be done in-place with O(1) extra space and O(n) time.

# Import helper utilities and Node type definitions from the project's Singly-linked list module.
from Singly import *


# Iterative in-place reversal of a singly linked list.
# Input: head node of the list; Output: new head node of the reversed list.
def reverseLinkedList(head: Node):
    # Start with current pointer at the head of the list.
    curr = head
    # 'prev' will hold the reversed list built so far; initialize to None (empty list).
    prev = None
    # Walk through the original list until we reach the end.
    while(curr != None):
        # Keep a reference to the current node; we'll rewire its next pointer.
        temp = curr
        # Advance curr to the next node in the original list before we overwrite links.
        curr = curr.next
        # Reverse the link for the temp node so it points to the previously-built reversed list.
        temp.next = prev
        # Move prev forward: temp is now the new head of the reversed portion.
        prev = temp
    # When curr is None we've processed all nodes; prev is the new head of reversed list.
    return prev


# Example data: a list of odd numbers to demonstrate reversal.
values = [1, 3, 5, 7, 9]
# Create a singly linked list from the example values using helper function.
head = createLinkedList(values)

# Print the original list to show precondition.
print("Original Linked List")
printLinkedList(head)

# Reverse the list using our function and print the result to verify correctness.
print("Reversed Linked List")
head = reverseLinkedList(head)
printLinkedList(head)

# Time complexity: O(n) where n is the number of nodes in the list (we visit each node once).
# Space complexity: O(1) additional space since we only use a few pointers regardless of list size.