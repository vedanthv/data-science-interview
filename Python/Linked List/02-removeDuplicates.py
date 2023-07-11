class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_duplicates(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current:
                data = current.data
                runner = current
                while(runner.next):
                    if runner.next.data == data:
                        runner = runner.next.next
                    else:
                        runner = runner.next
                current = current.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()