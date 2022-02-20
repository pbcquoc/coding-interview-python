class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None

def last_node(node):
    while node.next != None:
        node = node.next

    return node

def partition(l, h):
    x = h.data
    i = l.prev

    j = l

    while j != h:
        if j.data < x:
            i = l if i == None else i.next
            
            i.data, j.data = j.data, i.data

        j = j.next

    i = l if i == None else i.next
    i.data, h.data = h.data, i.data
    
    return i

def _quicksort(l, h):
    if h != None and l != h and l != h.next:
        tmp = partition(l, h)
        _quicksort(l, tmp.prev)
        _quicksort(tmp.next, h)

def quicksort(node):
    head = last_node(node)
    _quicksort(node, head)

def print_list(head):
    while(head != None):
        print(head.data, end=" ");
        head = head.next;

head = None
def push(new_data):
    global head
    new_node= Node(new_data)

    if head == None:
        head = new_node
        return

    new_node.next = head
    head.prev = new_node
    new_node.prev = None
    head = new_node


push(5);
push(20);
push(4);
push(3);
push(30);

print_list(head)
print('\n')
quicksort(head)
print_list(head)
