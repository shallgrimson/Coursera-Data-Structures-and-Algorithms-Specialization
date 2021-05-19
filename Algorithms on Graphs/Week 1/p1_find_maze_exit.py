'''
Problem 1 - Finding an Exit from a Maze
Input - [# nodes, # edges ,[data],start, goal]
Output - return 1 if can get from start to goal else 0
'''

import sys

#depth first search
def dfs(adj, visited, i, goal):
    visited[i] = 1
    for neighbour in adj[i]:
        if visited[goal] == 1: ##if we have seen goal just return
            return 1
        
        if visited[neighbour] == 0:
            dfs(adj, visited, neighbour, goal)
    
    return visited[goal]
        

if __name__ == '__main__':
    input = sys.stdin.readline() #I changed this from read() to readline()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    x, y = data[(2 * m):]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited =[0 for _ in range(n)]
    x, y = x - 1, y - 1 #this is just due to how they input the data
    for (a, b) in edges: #add notes to 2D graph
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    print(dfs(adj, visited, x, y))