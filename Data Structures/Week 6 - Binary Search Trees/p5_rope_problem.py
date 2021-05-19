'''
Problem 5 - Rope

Make use of the modified splay tree from the previous problem
#This works but using code from previous example, could definetly speed it up and maybe condense the process function
'''

import sys
from collections import deque
# Vertex of a splay tree
#################################################################################################### splay tree implementation
class Vertex:
  def __init__(self, key, letter, left, right, parent):
    (self.key,self.letter, self.left, self.right, self.parent) = (key, letter, left, right, parent)

def update(v):
  if v == None:
    return
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (next, root)

def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)  
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)

  
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

root = None


################################################################
  
# Code that uses splay tree to solve the problem

class Rope:
  def __init__(self, s):
    global root
    self.s = s
    prev = None #left Node
    p = None #parent Node
    
    for i, c in enumerate(s): ##apparently faster to not use insert here but create manually, tree will look like 0-0-0-0-0-0-0
      cur = Vertex(i, c, prev, None, None)  
      if prev:
        prev.parent = cur
      prev = cur
    root = cur
      
      

  def result(self, q, node):
    if node:
      q = self.result(q, node.left)
      q=q+node.letter
      q = self.result(q, node.right)
    
    return q

  def updateNode(self, top, i):
    q = deque()
    q.append(top)

    while q:
      deq = q.popleft()
      deq.key = deq.key + i
      
      if deq.left:
        q.append(deq.left)

      if deq.right:
        q.append(deq.right)
      
    return top


  def process(self, i, j, k):
    global root 
    (left, middle) = split(root, i) #split into elements that will be left of first index of current string
    (middle, right) = split(middle, j+1) #
    middle = self.updateNode(middle, k-j)
    if k==j:
      k+=1
      
    if k > j:
      (right, rightright) = split(right, k+1)
      right = self.updateNode(right,j-k)
      m1 = merge(left,right)
      m2 = merge(middle, rightright)
      root = merge(m1, m2)

    if k < i:
      if k>0: #could remove this but saves having to do a split, may have to move this
        (leftleft, left) = split(left, k)
      else:
        leftleft = None
      left = self.updateNode(left,i-k)
      m1 = merge(leftleft,middle)
      m2 = merge(left, right)
      root = merge(m1, m2)




      


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result("", root))