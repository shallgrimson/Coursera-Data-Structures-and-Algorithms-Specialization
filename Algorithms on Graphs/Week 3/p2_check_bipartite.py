'''
Problem 2 - Check if the graph is a bipartite

bipartite - A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) 
either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), 
either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.
'''
import sys
from queue import Queue #THIS MAY HAVE TO BE CHANGED TO queue to get this to work on grader

'''
Check if bipartite
Idea: Use breath first search to go through each neighbour of the current node and assign it to the other group, if we have already seen this neighbour check that it is in the other group.  If not than it cannot be a
bipartite

Input: array where index is the note and its data are the index neighbours
Output: 0 - Non bipartite
        1 - bipartite
        
IF ALL NODES ARE CONNECT THEN UNCOMMENT BELOW AND USE THAT, IT WILL BE FASTER ( JUST REMOVE GROUPS FROM PRINT STATEMENT)
'''
def dfs(adf, s, groups):
    groups[s] = 1 #initialize first node to set 1
    q = Queue()
    q.put(s)
    while not q.empty():
        cur = q.get() #get top of queue
        for neighbour in adj[cur]:
            if groups[neighbour] == 0: #if have not seen node before
                q.put(neighbour) #add neightbour to queue
                groups[neighbour] = 2 if groups[cur] == 1 else 1 #assign to opposite group of current node
            else:
                if groups[cur] == groups[neighbour]:
                    return 0, []
                
    return 1, groups

    
def bipartite(adj, s):
    groups = [0 for i in range(len(adj))] #initialize array to store if node needs to be in set 1 ore 2
    for i in range(len(groups)):
        if groups[i] == 0:
            check, groups = dfs(adj, i, groups)
            if check == 0:
                return 0
    
    return 1

#################################    
# just uncomment this if the nodes are all connected
#################################
# def bipartite(adj, s):
#     groups = [0 for i in range(len(adj))] #initialize array to store if node needs to be in set 1 ore 2
#     groups[s] = 1 #initialize first node to set 1
#     q = Queue()
#     q.put(s)
#     while not q.empty():
#         cur = q.get() #get top of queue
#         for neighbour in adj[cur]:
#             if groups[neighbour] == 0: #if have not seen node before
#                 q.put(neighbour) #add neightbour to queue
#                 groups[neighbour] = 2 if groups[cur] == 1 else 1 #assign to opposite group of current node
#             else:
#                 if groups[cur] == groups[neighbour]:
#                     return 0
                
#     return 1

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [4,4,1,2,4,1,2,3,3,1]
    #data = [5,4,5,2,4,2,3,4,1,4]
    #data = [8,7,0,4,0,5,1,6,2,5,3,7,2,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj, 0))