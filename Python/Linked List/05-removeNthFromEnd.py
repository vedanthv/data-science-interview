class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

def length_llist(llist):
    length = 0
    current = llist.head
    while current:
        current = current.next
        length = length + 1
    return length

def return_n_from_last(llist, n):
    l = length_llist(llist)
    current = llist.head
    for i in range(l - n):
        current = current.next
    return current.data

