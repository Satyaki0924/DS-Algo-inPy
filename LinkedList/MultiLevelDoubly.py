class Node:
    value = None; next = None; prev = None; child = None
    def __init__(self, value = 0, next = None, prev = None, child = None):
        self.value = value
        self.next = next
        self.prev = prev
        self.child = child
        pass

def createDoublyLinkedList(values: int) -> Node:
    if len(values) <= 0:
        return None
    head = Node(value=values[0])
    curr = head
    lineHead = head
    startNewLine = False
    skips = 0
    for i in range(1, len(values)):
        value = values[i]
       
        # same line end -> null
        if value == None:
            if not startNewLine:
                startNewLine = True
            
            else:
                skips += 1
            continue
        else:
            if startNewLine:
                startNewLine = False
                curr = Node(value = value)
                while skips > 0 and lineHead != None:
                    skips -= 1
                    lineHead = lineHead.next
                lineHead.child = curr
                lineHead = curr
                continue
        
        newNode = Node(value=value)
        curr.next = newNode
        newNode.prev = curr
        curr = curr.next
    return head
    
def visualize_multilevel_list(head: Node, level=0, visited=None):
    """Recursively print the multilevel doubly linked list with indentation."""
    if visited is None:
        visited = set()  # prevent infinite recursion
    curr = head
    prefix = "    " * level
    while curr:
        if curr in visited:
            print(prefix + f"↩️ (cycle detected at {curr.value})")
            return
        visited.add(curr)
        print(prefix + f"{curr.value}", end="")
        if curr.next:
            print(" ↔ ", end="")
        else:
            print(" -> None", end="")
        if curr.child:
            print("\n" + prefix + "  |")
            print(prefix + "  └─ Child of", curr.value)
            visualize_multilevel_list(curr.child, level + 1, visited)
        curr = curr.next
    print()

def printDoublyList(head: Node):
    if head == None or head.value == None:
        return None
    print(head.value)
    printDoublyList(head.child)
    printDoublyList(head.next)

