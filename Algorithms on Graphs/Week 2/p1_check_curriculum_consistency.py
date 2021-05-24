'''
Problem 1 - Check consistency of a curriculum

Right now assuming all nodes in graph are connected
'''
import sys

#use depth first search to find if cycles
def dfs(adj, i, visited, inner_visit):
    visited[i] = 1
    inner_visit[i] = 1

    for n in adj[i]:
        if visited[n] == 0:
            out, visited = dfs(adj, n, visited, inner_visit)
        
        if inner_visit[n] == 1 or out == 1: #if have been to this node before within the recursion
            return 1, []
    
    inner_visit[i] = 0 #reset for next look through, as can have two nodes point to the same node

    return 0, visited

#check if cycles in the graph
def acyclic(adj):
    visited = [0 for i in range(len(adj))]
    inner_visit = [0 for i in range(len(adj))] #use to check for cycles in each look through

    for i in range(len(adj)):
        if visited[i] == 0:
            out, visited = dfs(adj, i, visited, inner_visit) 
        
        if out == 1:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [4,4,1,2,4,1,2,3,3,1] #output should be 1 - has cycles
    #data = [5,7,1,2,2,3,1,3,3,4,1,4,2,5,3,5] #output should be 0 - no cycles
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))