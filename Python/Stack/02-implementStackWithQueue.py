class Stack:
    def __init__(self):
        self.q = Queue()
 
    def is_empty(self):
        return self.q.is_empty()
 
    def push(self, data):
        self.q.enqueue(data)

    # dequeue and enqueue from stack n-1 times
    def pop(self,data):
        for _ in range(self.q.get_size()-1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.queue.dequeue()

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.size += 1
        self.items.append(data)
 
    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)
 
    def get_size(self):
        return self.size

