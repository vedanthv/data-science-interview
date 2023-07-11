class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
 
    def append(self, data):
        self.insert_at_end(Node(data))
 
    def insert_at_end(self, new_node):
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

def find_largest(dllist):
    if dllist.first is None:
        return None
    largest = dllist.first.data
    current = dllist.first.next
    while current:
        if current.data > largest:
            largest = current.data
        current = current.next
    return largest