'''
Problem 4 - Construct the Suffix Tree of a String

Soln: create suffix tree - basically a suffix trie but single node branches are combined together
->append dollar-sign ("$") to end inorder to mark the end of the suffix
->only store first and last index in each node, start by making big suffix and then branching as needed
'''

import sys
import queue

class Node:
    def __init__(self, r):
        self.range = r
        self.next = []
        
'''
Split branch

Input: 
base - branch to be split
split_index - index where base branch and suffic do not align, based on branch index
suffix_range - range of new branch
'''
def node_split(base, split_index, suffix_range):

    end_index = base.range[1]
    base.range[1] = split_index - 1

    new_node = Node([split_index, end_index]) #splitted node
    new_node.next=base.next 
    base.next=[Node(suffix_range), new_node] #create new node

    
    
"""
Build a suffix tree of the string text and return a list
with all of the labels of its edges (the corresponding 
substrings of the text) in any order.
"""
def build_suffix_tree(text):
  result = []
  final_index = len(text)-1
  root = Node([-1, -1]) #create root
  root.next.append(Node([0, final_index])) #add full text
  
  for i in range(1, final_index+1): #iterate through text
      cur_node = root #first look at root
      suffix_i = i
      while suffix_i <= final_index: 
        found = False #check if found any matches
        for branch_node in cur_node.next: #iterate through next nodes
          if text[suffix_i] == text[branch_node.range[0]]: #check if first letters are the same, means enter branch 
            found = True
            cur_node = branch_node #go to node where there is a match for next iteration
            suffix_i+=1
            for branch_i in range(branch_node.range[0]+1, branch_node.range[1]+1):
              if text[suffix_i] == text[branch_i]: #compare new suffix with current branch
                suffix_i+=1 #iterate to nxt
              else:
                node_split(cur_node, branch_i, [suffix_i, final_index])  #mismatch in node and suffix so split current node  
                suffix_i = final_index+1
                break
                
            break
            
        if found == False: #if no matches append suffixto current node
            cur_node.next.append(Node([suffix_i, final_index]))
            break
            
      
###get all branches of suffix tree
  q = queue.Queue()
 # print("------rooot-----")
  for n in root.next:
  #  print(text[n.range[0]:n.range[1]+1])
    q.put(n)
  while not q.empty():
    cur = q.get()
    result.append(text[cur.range[0]:cur.range[1]+1])
 #   print('----------'+text[cur.range[0]:cur.range[1]+1]+'----------')
    for n in cur.next:
  #    print(text[n.range[0]:n.range[1]+1])
      q.put(n)

  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  #text = 'ACA$'
  #text = 'banana$'
  #text = 'panamabananas$'
  #text = 'MISSISSIPPI$'
  #text = 'AAAAAAA$'
  result = build_suffix_tree(text)
  print("\n".join(result))