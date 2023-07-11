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

def isEqual(list1,list2):
    curr1 = list1.head
    curr2 = list2.head

    while curr1 and curr2:
        if curr1.data != current2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False


if is_equal(llist1, llist2):
    print('The two linked lists are the same.')
else:
    print('The two linked list are not the same.', end = '')
