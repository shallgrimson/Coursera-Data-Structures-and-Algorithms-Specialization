'''
Set with range sums
'''
from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
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

  
# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
  root = merge(merge(left, new_vertex), right)
  
def erase(x): 
  global root
  # Implement erase yourself
  (node, root) = find(root, x)
  if node and node.key == x:
    if node.right == None and node.left == None:
      root = None
      return
    
    (left, middle) = split(root, x)
    if middle.right == None:
      root = left
      return

    (middle, right) = split(middle, x+1)
    merge(left,right)

#########Another soln
#   if node and node.key == x:
#     #splay(node.parent) #first bring parent to top
#     #splay(node) #then bring current node
#     if node.left == None and node.right == None:
#         root = None
#     elif node.left == None:
#         node.right.parent = None
#         root = node.right
#     elif node.right == None:
#         node.left.parent = None
#         root = node.left
#     else:
#         merge(node.left, node.right) #merge left and right halfs


def search(x): 
  global root
  (res, root) = find(root, x)
  if res and res.key == x:
      return True

  return False
  
def sum(fr, to): 
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0
  # Complete the implementation of sum
  if middle:
      ans = middle.sum

  return ans

MODULO = 1000000001
n = int(stdin.readline())

#lines = [["?","1"],["+","1"],["?","1"],["-","1"],["?","1"],["+","3"],["-","6"],["?","6"],["s","3","4"]]
#lines = [["?",1],["+",1],["?",1],["+", 2],["s",1,2],["+",1000000000],["?",1000000000],["-",1000000000],["?",1000000000],["s",999999999, 1000000000],["-",2],["?",2],["-",0],["+",9],["s",0,9] ]
#n = len(lines)

last_sum_result = 0
for i in range(n):
  #line = lines[i]
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO