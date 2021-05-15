'''
Binary Tree Traversals
Goal - Implement in-order, pre-order and post-order traversals of a binary tree
'''
import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
####### READ INPUTS
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

######## IN ORDER TRAVERSAL
  def inOrder(self):
    result = []

######## RECURSIVE FUNCTION
    def inOrderRecursion(index):
        if index == -1:
            return

        inOrderRecursion(self.left[index])
        result.append(self.key[index])
        inOrderRecursion(self.right[index])

    inOrderRecursion(0)
                
    return result

######## PRE ORDER TRAVERSAL
  def preOrder(self):
    result = []

######## RECURSIVE FUNCTION
    def preOrderRecursion(index):
        if index == -1:
            return
        result.append(self.key[index])
        preOrderRecursion(self.left[index])
        preOrderRecursion(self.right[index])

    preOrderRecursion(0)

    return result

######## POST ORDER TRAVERSAL
  def postOrder(self):
    result = []

######## RECURSIVE FUNCTION
    def postOrderRecursion(index):
        if index == -1:
            return

        postOrderRecursion(self.left[index])
        postOrderRecursion(self.right[index])
        result.append(self.key[index])

    postOrderRecursion(0)
                
    return result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()