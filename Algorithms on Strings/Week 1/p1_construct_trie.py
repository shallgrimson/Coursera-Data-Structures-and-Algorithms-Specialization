'''
Problem 1 - Construct a trie from a sequency of patterns
'''

#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    node_cnt = 1 #used to track number of nodes
    for p_i in patterns:
        cur_node = 0 #start at root
        for c in p_i:
            print(c,cur_node,node_cnt,tree[cur_node])
            if c not in tree[cur_node]: #if letter not in tree add it
                tree[cur_node][c] = node_cnt #add letter that sub-dictionary
                tree[node_cnt] = dict() #create new dictionary for letter
                cur_node = node_cnt #move to new dictionary
                node_cnt+=1
            else:
                cur_node = tree[cur_node][c] #find index of that letter in sub-dictionary
    
    return tree


if __name__ == '__main__':
    #patterns = sys.stdin.readline().split()[1:]
    patterns = ['AAA']
    #patterns=['ATAGA','ATC','GAT']
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))