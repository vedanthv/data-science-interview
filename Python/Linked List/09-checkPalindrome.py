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
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
 
def is_palindrome(llist):
    start = llist.head
    end = llist.last_node
    while (start != end and end.next != start):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True
