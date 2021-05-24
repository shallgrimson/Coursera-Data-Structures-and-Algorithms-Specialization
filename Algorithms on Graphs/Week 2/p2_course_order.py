'''
Problem 3 - Determine an order of courses

Use topological ordering of a directed acyclic graph(DAG)
'''
import sys

#perform depth first search
def dfs(adj, used, order, x):
    used[x] = 1
    for neighbour in adj[x]:
        if used[neighbour] == 0:
            order, used = dfs(adj, used, order, neighbour)
        
    order.append(x)
    return order, used

#main func
def toposort(adj):
    used = [0] * len(adj)
    order = []
    
    for i in range(len(adj)):
        if used[i] == 0:
            order, used = dfs(adj, used, order, i)
    
    return order

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [4,3,1,2,4,1,3,1]
    #data = [4,1,3,1]
    #data=[5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    s=''
    for x in order:
        s = str(x+1)+' '+s #print in reverse order
    print(s)
