'''
Problem 4 - Extending stack interface
#saves max element in each value element using math
'''
class Node:
    def __init__(self, inData):
        self.data=inData
        self.next=None

class Stack:
    def __init__(self):
        self.head = None
        self.max = None 
        self.maxElement=None

    def push(self, data):
        if self.head == None:
            self.maxElement = data
            ndata = data
        else:
            if data > self.maxElement:
                ndata = 2*data + self.maxElement
                self.maxElement = data
            else:
                ndata = data
        
        newNode = Node(ndata)
        newNode.next = self.head
        self.head = newNode
        

    def pop(self):
        if self.head.data > self.maxElement:
            self.maxElement = self.head.data-2*self.maxElement

        self.head = self.head.next
    
    def maxEle(self):
        print(self.maxElement)

    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

def minStack_interface(n, commands):
    s = Stack()
    for i in range(n):
        c=commands[i].split()
        if c[0]=='push':
            s.push(int(c[1]))
        elif c[0]=='pop':
            s.pop()
        elif c[0]=='max':
            s.maxEle()

if __name__ == "__main__":
    commands = ['push 2', 'push 1', 'max', 'pop', 'max']
    minStack_interface(len(commands), commands)

    print("-----------")
    commands = ['push 1', 'push 2', 'max', 'pop', 'max']
    minStack_interface(len(commands), commands)

    print("-----------")
    commands = ['push 2', 'push 3', 'push 9', 'push 7', 'push 2', 'max', 'max', 'max', 'pop', 'max']
    minStack_interface(len(commands), commands)

    print("-----------")
    commands = ['push 1', 'push 7', 'pop'] #no max queriers so empty
    minStack_interface(len(commands), commands)


    print("-----------")
    commands = ['push 7', 'push 1', 'push 7', 'max', 'pop', 'max']
    minStack_interface(len(commands), commands)

    