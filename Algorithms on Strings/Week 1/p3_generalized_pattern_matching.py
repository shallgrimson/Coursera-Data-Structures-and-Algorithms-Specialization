'''
Problem 3 - Generalized Mulitple Pattern Matching

Goal: return index of first character of when multiple patterns exist in some string
'''
# python3
import sys

class Node:
    def __init__(self, i):
        self.i = i
        self.isPattern=False #some deliminator in the trie could have just been done to do this
    
	#reusing code from previous problem
def build_trie(patterns):
	root = dict()
	root[0] = dict() #create root in dictionary
	node_cnt = 1
	for p_i in patterns:
		cur_node = 0 #start at root
		for c in p_i:

			prev_node = cur_node
			if c not in root[cur_node]: #if letter not in tree add it
				root[cur_node][c] = Node(node_cnt) #add letter that sub-dictionary
				root[node_cnt] = dict() #create new dictionary for letter
				cur_node = node_cnt #move to new dictionary
				node_cnt+=1
			else:
				cur_node = root[cur_node][c].i #find index of that letter in sub-dictionary

		root[prev_node][p_i[-1]].isPattern = True
	return root

 
def solve (text, n, patterns):
	result = []
	pat_trie = build_trie(patterns)

	i = 0
	while i < len(text):
		suffix = i
		node = 0 #start at root
		while suffix<len(text) and text[suffix] in pat_trie[node]: 

			if pat_trie[node][text[suffix]].isPattern: #check if this is a patern
				result.append(i)
				break
			node = pat_trie[node][text[suffix]].i #move to new nodes dictinary
			suffix+=1
    
		i+=1
  
     
	return result


if __name__ == '__main__':
	# text = sys.stdin.readline().strip()
	# n = int(sys.stdin.readline().strip())
	# patterns = []
	# for i in range (n):
	# 	patterns += [sys.stdin.readline ().strip ()]
	text = 'ACATA'
	n=3
	patterns = ['AT','A','AG']
	# text='AAA'
	# n=1
	# patterns=['AA']
	ans = solve (text, n, patterns)
	sys.stdout.write (' '.join (map (str, ans)) + '\n')