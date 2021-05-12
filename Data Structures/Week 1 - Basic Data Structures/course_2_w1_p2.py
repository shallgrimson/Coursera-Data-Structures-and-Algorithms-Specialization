###using python 2.7.6
'''
Problem 2 - compute tree height --tree could

left and right are indexes of the next node
so I create an array, each element in array is then a node.
\->the left and right element are just integers holding the index of the next child
'''
class Node:
    def __init__(self, inData = None):
        self.data = inData
        self.left = None #index of left child
        self.right = None #index of right child


#root stored at 1 and everything else stored after
def find_tree_height(treeSize, data):
    if treeSize <= 1:
        return treeSize
    #inner func to find height
    def getHeight(h, n):
        lh, rh = h+1, h+1

        if n.left is not None:
            lh = getHeight(lh, tree[n.left])
        if n.right is not None:
            rh = getHeight(rh, tree[n.right])
        
        return max(lh, rh)

  
    tree = [Node(i) for i in range(len(data))]
        
    #code to build tree
    index = 0 #could just use enumerate
    head = 0 #index of head in tree
    for e in data:
        #print(index)
        if e == -1:
            head = index
        else:
            if tree[e].left == None:
                tree[e].left = index
            else:
                tree[e].right = index 
        
        index = index+1
    
    return getHeight(0, tree[head])






if __name__ == "__main__":
    # arr = [Node()]*4
    # print(arr[0].data)

    print(find_tree_height(5, [4,-1,4,1,1]))
    print(find_tree_height(5, [-1,0,4,0,3]))
    print(find_tree_height(2, [-1,0]))
