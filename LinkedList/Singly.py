class Node:
    value, next = None, None
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def createLinkedList(values: list) -> Node:
    if len(values) <= 0:
        return None
    head = Node(values[0])
    curr = head
    for i in range(1, len(values)):
        curr.next = Node(values[i])
        curr = curr.next
    return head

def createCyclicLinkedList(values: list, pos: int) -> Node:
    if len(values) <= 0:
        return None
    head = Node(values[0])
    tail = head
    for i in range(1, len(values)):
        tail.next = Node(values[i])
        tail = tail.next

    curr = head
    for i in range(pos):
        curr = curr.next
    tail.next = curr
    return head

def printLinkedList(head: Node):
    while(head != None):
        print(head.value)
        head = head.next