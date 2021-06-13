'''
Problem 4 -Construct the Suffix Tree from the Suffix Array

Construct a suffix tree from the suffix array and LCP array of a string.
LCP - Longest common prefix
'''
import sys
import queue
from collections import OrderedDict, deque
'''
This is from problem 2
'''
###############################################################################
#return character index of character, $=0,A=1,B=2.....
def get_character_index(c):
    if c == '$': #COULD JUST PUT THIS DIRECTLY INTO COUNT SINCE KNOW IT WILL BE LAST POSITION
        return 0
    return ord(c)-64 #ord('A')=65, then set A as index 1
    
#sort charactes in text using count sort
#could directly add $ into this!!!!!
def sort_characters(S):
    order = [0 for _ in range(len(S))]
    count = [0 for _ in range(26)] #26 letters in the alphabet
    
    for c in S:
        count[get_character_index(c)]+=1 #ord('A')=65
    for j in range(1, 26):
        count[j] = count[j-1] + count[j]
        
    for i in range(len(S)-1,-1,-1):
        c=get_character_index(S[i]) #could seperate this in its own function
        count[c] -= 1
        order[count[c]] = i
    
    return order

#sort charcters of string into similar groups
def compute_char_classes(S, order):
    char_classes = [0 for _ in range(len(S))]
    char_classes[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            char_classes[order[i]] = char_classes[order[i-1]]+1
        else:
            char_classes[order[i]] = char_classes[order[i-1]]
    
    return char_classes
    
    
def sort_double(S,L,order,char_classes):
    count = [0 for _ in range(len(S))]
    newOrder = [0 for _ in range(len(S))]
    for i in range(len(S)):
        count[char_classes[i]] = count[char_classes[i]]+1
    for j in range(1,len(S)):
        count[j] = count[j]+count[j-1]
    
    for i in range(len(S)-1,-1,-1):
        start = (order[i]-L+len(S))%len(S)
        cl = char_classes[start]
        count[cl] = count[cl] - 1
        newOrder[count[cl]] = start
    
    return newOrder

def update_classes(newOrder, char_classes, L):
    n = len(newOrder)
    newCharClass = [0]*n
    newCharClass[newOrder[0]] = 0
    for i in range(1, n):
        prev, cur = newOrder[i-1], newOrder[i]
        midPrev, mid = (prev+L)%n,(cur+L)%n
        if char_classes[cur] != char_classes[prev] or char_classes[mid] != char_classes[midPrev]:
            newCharClass[cur] = newCharClass[prev]+1
        else:
            newCharClass[cur] = newCharClass[prev]
    
    return newCharClass

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = sort_characters(text)
  char_classes = compute_char_classes(text, order)
  L = 1
  while L < len(text):
      order = sort_double(text,L,order,char_classes)
      char_classes = update_classes(order,char_classes,L)
      L=2*L
  # Implement this function yourself
  return order
###############################################################################
class SuffixTreeNode:
    def __init__(self, parent, depth, start, end):
        self.parent=parent
        self.children=OrderedDict()
        self.stringDepth=depth
        self.edgeStart=start
        self.edgeEnd=end

#create new node
def CreateNewLeaf(node, text, suffix,n):
    leaf = SuffixTreeNode(node, n-suffix, suffix+node.stringDepth, n-1)
    node.children[text[leaf.edgeStart]] = leaf
    return leaf

#break an edge to seperate into 2 nodes 
def BreakEdge(node, text,start,offset):
    startChar = text[start]
    midChar = text[start+offset]
    midNode = SuffixTreeNode(node, node.stringDepth+offset, start, start+offset-1)
    midNode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midNode
    node.children[startChar].edgeStart = offset
    node.children[startChar] = midNode
    return midNode

#func input:suffix array, array of least common prefix, text
def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label
    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    n=len(text)
    tree = {}
    tree[0]=[]
    root=SuffixTreeNode(None,0,-1,-1)
    lcpPrev = 0
    curNode = root #start at root
    for i in range(n):
        suffix = sa[i]
        while curNode.stringDepth > lcpPrev:
            curNode=curNode.parent
        if curNode.stringDepth == lcpPrev:
            curNode = CreateNewLeaf(curNode,text,suffix,n)
        else:
            edgeStart = sa[i-1]+curNode.stringDepth
            offset = lcpPrev-curNode.stringDepth
            midNode=BreakEdge(curNode,text,edgeStart,offset)
            curNode=CreateNewLeaf(midNode,text,suffix,n)
        if i < n-1:
            lcpPrev = lcp[i]
            
    return root   
    #return tree


if __name__ == '__main__':
    #text = sys.stdin.readline().strip()
    #sa = list(map(int, sys.stdin.readline().strip().split()))
    #lcp = list(map(int, sys.stdin.readline().strip().split()))
    text='AAA$'
    sa = [3,2,1,0]
    lcp = [0,1,2]
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    
    q = []
    for _, neighbour in tree.children.items():
        q.append(neighbour)
    while q:
        c = q.pop()
        print(c.edgeStart, c.edgeEnd)
        for _,n in c.children.items():
            q.append(n)
    
    # q = deque()
    # for _, neighbour in tree.children.items():
    #     q.append(neighbour)
    # while q:
    #     cur = q.popleft()
    #     print(cur.edgeStart, cur.edgeEnd)
    #     for key, neighbour in cur.children.items():
    #         print(key)
    #         q.appendleft(neighbour)
            
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    #this need to change with the current implementation that I have
    # stack = [(0, 0)]
    # result_edges = []
    # while len(stack) > 0:
    #   (node, edge_index) = stack[-1]
    #   stack.pop()
    #   if not node in tree:
    #     continue
    #   edges = tree[node]
    #   if edge_index + 1 < len(edges):
    #     stack.append((node, edge_index + 1))
    #   print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
    #   stack.append((edges[edge_index][0], 0))