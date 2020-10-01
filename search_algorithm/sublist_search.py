# Given two linked lists, the task is to check whether the first list is present in 2nd list or not. 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_list(first, second):

    while second:
        ptr2 = second
        ptr1 = first

        while ptr1:
            if not ptr2:
                return False
            elif ptr1.value == ptr2.value:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            else:
                break
        
        if not ptr1:
            return True

        second = second.next
        
    return False

node_a = Node(1) 
node_a.next = Node(2) 
node_a.next.next = Node(3) 
node_a.next.next.next = Node(4) 
  
node_b = Node(1) 
node_b.next = Node(2) 
node_b.next.next = Node(1) 
node_b.next.next.next = Node(2) 
node_b.next.next.next.next = Node(5) 
node_b.next.next.next.next.next = Node(4)         

r = find_list(node_a, node_b)
print(r)
