# Import everything from the helper module that defines the Node class and list constructors.
# We rely on createDoublyLinkedList and Node definitions from MultiLevelDoubly.
from MultiLevelDoubly import *


# Traverse a child doubly-linked list and return its head and tail nodes.
# We need both because when splicing the child list into the parent, we must connect both ends.
def returnChildHeadTail(childHead: Node):
    # Start traversal from the provided head of the child list.
    curr = childHead
    # Initialize childTail as childHead; it will move to the actual tail during traversal.
    childTail = childHead
    # Walk the next pointers until we reach the end (None).
    while curr != None:
        # Keep updating childTail so it always points to the last visited node.
        childTail = curr
        # Move to the next node in the child list.
        curr = curr.next
    # Return a tuple of (head, tail) for the child list to facilitate splicing.
    return(childHead, childTail)
        
        
# Problem: 430. Merge a Multilevel Doubly Linked List
# Flatten a multilevel doubly linked list in-place and return the head of the flattened list.
# The algorithm splices each node's child list (if present) between the node and its next node.
def flattenDoublyList(head: Node) -> Node:
    # Handle empty list input quickly by returning None.
    if head == None:
        return None
    
    # Start processing from the head of the top-level list.
    curr = head

    # Iterate through the list using next pointers; when we splice a child list we continue from there.
    while curr != None:

        # If the current node has a child, splice the entire child list into the main list here.
        if curr.child != None:
            # Get the head and tail of the child list so we can connect both ends.
            childHead, childTail = returnChildHeadTail(curr.child)
            # Remove the child pointer after we grab the child list (we're flattening it).
            curr.child = None
            # Temporarily save the current node's next pointer to reconnect after the child list.
            temp = curr.next
            
            # Connect current node to the head of the child list.
            curr.next = childHead
            # Maintain doubly-linked prev link from child head back to current node.
            childHead.prev = curr

            # Connect the tail of the child list to the saved next node (temp).
            childTail.next = temp
            # If there was a next node after curr, update its prev to point to the child tail.
            if temp != None:
                temp.prev = childTail

        # Move on to the next node; after splicing this will traverse into the child region first.
        curr = curr.next
    
    # Return the head of the now-flattened list.
    return head


# Helper to print values of a singly-seen traversal of the (now flattened) doubly-list.
# We print values in-order following next pointers only for demonstration.
def printSinglyLinkedlist(head: Node):
    # Print an empty list representation if head is None.
    if head == None:
        print([])
        return
    # Walk the list using next pointers and print each node's value.
    while head != None:
        print(head.value, end = " ")
        head = head.next


# Example 1: test a complex multilevel list represented by the `values` encoding used by helper.
# The comment shows the expected flattened order for reference.
values = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12] # [1,2,3,7,8,11,12,9,10,4,5,6]
# Build the multilevel doubly list using the helper from MultiLevelDoubly.
head = createDoublyLinkedList(values=values)
# Flatten the list in-place.
head = flattenDoublyList(head)
# Print the flattened sequence of node values.
printSinglyLinkedlist(head)

print()
# Example 2: another small test; expected flattened order shown in comment.
values = [1,2,None,3] # [1,3,2]
head = createDoublyLinkedList(values=values) 
head = flattenDoublyList(head)
printSinglyLinkedlist(head)

print()
# Example 3: empty input should produce an empty output.
values = [] # []
head = createDoublyLinkedList(values=values) 
head = flattenDoublyList(head)
printSinglyLinkedlist(head)

# Time complexity: O(n) where n is the total number of nodes across all levels.
# Space complexity: O(1) additional space since we modify the list in place.