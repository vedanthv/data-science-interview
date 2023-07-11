class implStack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return self.stack == []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()

s = Stack()

while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
