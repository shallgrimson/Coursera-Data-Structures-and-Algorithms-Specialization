###using python 2.7.6
'''
Problem 1 - the first bit is the data structure
'''
class node:
    def __init__(self, d=None, n=None):
        self.data = d
        self.next = n
    
    def __repr__(self):
        return self.data
    


#linked list
class linkedList:
    def __init__(self):
        self.head = None
    
    #push node to front of linked list
    def pushFront(self, data): 
        newNode = node(data, self.head)
        self.head = newNode

    def popTop(self):
        self.head = self.head.next
    
    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

        
#stack
class stack:
    def __init__(self):
        self.__baseList = linkedList()
        self.__size = 0

    def  push(self, data):
        self.__baseList.pushFront(data)
        self.__size+= 1

    def top(self):
        return self.__baseList.head.data

    def pop(self):
        self.__baseList.popTop()
        self.__size-=1
    
    def empty(self):
        return not self.__size

    def printStack(self):
        self.__baseList.printList()


'''
Problem 1 - Check brackets in the code
'''
def checkParentheses(s):
    statStack = stack()
    for index, c in enumerate(s): 
        if c == '(' or c == '[' or c == '{':
            statStack.push(c)
        elif c == ')' or c == ']' or c == '}':
            if statStack.empty():
                return index

            top = statStack.top()

            if (c == ')' and top != '(') or  (c == ']' and top != '[') or  (c == '}' and top != '{'):
                return index+1
            

            statStack.pop() #check good so pop top
            
    if not statStack.empty(): #this could be be sped up by saving indexes as well
        return s.find(statStack.top())+1

    return 'Success'  


if __name__ == "__main__":
    # l = linkedList()
    # l.pushFront(5)
    # l.pushFront(4)
    # l.pushFront(2)
    # l.printList()

    # s = stack()
    # print(s.empty())
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # s.push(4)
    # print(s.top())
    # s.printStack()
    # print("-----")
    # s.pop()
    # s.printStack()
    
 
    print(1, checkParentheses('[]'))
    print(2, checkParentheses('{}[]'))
    print(3,checkParentheses('[()]'))
    print(4, checkParentheses('(())'))
    print(5, checkParentheses('{[]}()'))
    print(6, checkParentheses('{'))
    print(7, checkParentheses('{[}'))
    print(8, checkParentheses('foo(bar)'))
    print(9, checkParentheses('foo(bar[i);'))
