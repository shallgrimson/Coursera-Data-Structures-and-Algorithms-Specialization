'''
Problem 3 - Checking Whether Any Intersection in a City is Reachable from Any Other
Steps:
1 - get reverse graph - Done
2 - run DFS on graph and get post order of each node
3 - iterate through reverse postorder
    3.1 if have not seen node before
        3.1.2 explore node
        3.2.3 mark visited vertices as SCC
'''
import sys

sys.setrecursionlimit(200000)

#get reverse of input direction graph
def get_reverse_graph(n, adj):
    revadj = [[] for _ in range(n)]
    for node in range(n):
        for rev in adj[node]:
            revadj[rev].append(node)
    
    return revadj

#perform depth first search
def dfs(adj, visited, postorder, i, clock):
    visited[i] = 1
    clock = clock + 1
    for neighbour in adj[i]:
        if visited[neighbour] == 0:
            postorder, visited, clock = dfs(adj, visited, postorder, neighbour, clock)
        
    postorder[i] = clock
    clock = clock + 1
    return postorder, visited, clock

#explore function
def explore(adj, visited, i):
    visited[i] = 2
    for neighbour in adj[i]:
        if visited[neighbour] == 1:
            visited = explore(adj, visited, neighbour)
    
    return visited
    


#main func
def number_of_strongly_connected_components(n, adj):
    visited = [0]*n
    postorder = [0]*n
    clock = 0
    
    #get reverse graph
    revadj = get_reverse_graph(n, adj)
    
    #perform depth first search of reverse graph to get postorder
    for i in range(n):
        if visited[i] == 0:
            postorder, visited, clock = dfs(revadj, visited, postorder, i, clock)
    
    #sort post order in reverse order
    reversepost = sorted(range(n), key=lambda k: postorder[k], reverse=True)

    #explore each node in reverse order, nodes found are part of the same strongly connected group
    #visited = [0]*n
    scc_cnt = 0
    for i in reversepost:
        if visited[i] == 1:
            scc_cnt+=1
            visited = explore(adj, visited, i)

    return scc_cnt
        



if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [4,4,1,2,4,1,2,3,3,1] #output: 2
    #data=[5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3] #output: 5
    #data=[9,13,1,2,2,5,2,4,3,2,4,3,4,7,4,1,6,5,6,7,7,6,8,7,9,8,9,1] #output: 5
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    
    print(number_of_strongly_connected_components(n, adj))