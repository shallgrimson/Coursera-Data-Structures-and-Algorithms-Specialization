'''
Problem 5 - Maximum in Sliding Window
Use doubled ended queeue
For each elements push to the left (head) and remove from the right (tail)
when adding elements check if head element is < element being added and if it is pop it (keep going until next element is bigger or at end of queue)
-then only pop tail end if it leaves the window

###can improve this by just saving indexes### this would probably speed it up and reduce space, just use previous dequege calseses to do this, disjoint dequege from class and put all the 
'''
class Node:
    def __init__(self, d, i):
        self.index = i
        self.next = None
        self.prev = None

    

class Dequeue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #pop newest element
    def popHead(self):
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None #since now it is left most element
            
            

    #pop oldest
    def popTail(self):
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None #since now it is right most element


    def pushHead(self, data, index):
        newNode = Node(data, index)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    

    def getTailIndex(self):
        return self.tail.index

    def getMax(self):
        return self.tail.index

    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
            
def max_window(n, arr, w):
    if n == 0:
        return 
    
    q = Dequeue()

    for i, d in enumerate(arr):
        while q.head != None and d >= arr[q.head.index]:
            q.popHead()

        q.pushHead(d, i) #push new element

        if q.getTailIndex() < i-w+1: #remove tail if it is out of window
            q.popTail()

        if i >= w-1:
            print(arr[q.getMax()])
        


if __name__ == "__main__":
    arr = [2,7,3,1,5,2,6,2]
    max_window(len(arr), arr, 4)

    print("----------------")
    arr = [2,7,3,1,5,2,6,2]
    max_window(len(arr), arr, 2)