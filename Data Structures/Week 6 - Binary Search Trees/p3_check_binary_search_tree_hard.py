'''
Check if a binary search tree was implemented properly but includes properties that could be equal

I think this may be very slow
'''
import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size




def IsBinarySearchTree(tree):
#this could definetly be condensed
  # Implement correct algorithm here
    def isBSTRecursion(index, side): #1 means return max key (going left), 2 means return min key (going right)
        if index == -1:
            return tree[index][0]

        li = tree[index][1]
        ri = tree[index][2]
        b=True

        if li != -1:
            b, maxKey = isBSTRecursion(li, 1)
        else:
            maxKey = tree[index][0]-1
        
        if ri != -1:
            b, minKey = isBSTRecursion(ri, 2)
        else:
            minKey = tree[index][0]+1

        if b == False or (tree[index][0] <= maxKey) or (tree[index][0] > minKey):
            return False, 0

        if side == 1 and li!=-1:
            return  True, max(max(maxKey,tree[index][0]),minKey)
        
        if side == 2 and ri!=-1:
            return  True, min(min(minKey,tree[index][0]),maxKey)

        return True, tree[index][0]

    b,r = isBSTRecursion(0,0)

    return b


def main():
    nodes = int(sys.stdin.readline().strip())
    if nodes == 0:
        print("CORRECT")
        return

    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    #tree = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
    #tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")
    

if __name__ == "__main__":
    main()
