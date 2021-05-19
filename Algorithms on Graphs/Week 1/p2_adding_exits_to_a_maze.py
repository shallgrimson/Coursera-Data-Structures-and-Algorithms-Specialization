'''
Problem 2 -  Adding Exits to a Maze

Input - [# nodes, # edges ,[data],start, goal]
Output - Connected Components

Connected Components - Number of groups where two groups have 0 connected nodes (ex: CC = 2: 0-0 0-0-0)
'''
import sys

#depth first search
def dfs(adj, visited, i):
    visited[i] = 1
    for neighbour in adj[i]:        
        if visited[neighbour] == 0:
            dfs(adj, visited, neighbour)
    
    return visited

#get connected components
def get_connected_components(adj, n):
    visited =[0 for _ in range(n)]
    cc = 0 #connected components
    for i in range(n):
        if visited[i] == 0:
            cc+=1
            visited = dfs(adj,visited,i)
    
    return cc
    

if __name__ == '__main__':
    input = sys.stdin.readline() #I changed this from read() to readline()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]

    for (a, b) in edges: #add notes to 2D graph
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    print(get_connected_components(adj, n))