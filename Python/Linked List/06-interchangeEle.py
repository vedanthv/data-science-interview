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
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

def interchange(llist,m,n):
    node1 = llist.get_node(m)
    node2 = llist.get_node(n)

    prev_node1 = llist.get_prev_node(node1)
    prev_node_2 = llist.get_prev_node(node2)

    if prev_node_1 is not None:
        prev_node1.next = node2
    else:
        llist.head = node2
    
    if prev_node_2 is not None:
        prev_node_2.next = node1
    else:
        llist.head = node1
    
    temp = node2.next
    node2.next = node1.next
    node1.next = temp

a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
ans = input('Please enter the two indices of the two elements that'
            ' you want to exchange: ').split()
n = int(ans[0])
m = int(ans[1])
 
interchange(a_llist, n, m)
 
print('The new list: ')
a_llist.display()

