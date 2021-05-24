'''
Problem 3 - Exchanging Money Optimally

Soln:  Use Bellman Ford's algorithm
'''
import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0 #set start node value to 0
    reachable[s] = 1
    #run through distances once
    for _ in range(len(adj)):
        for node in range(len(adj)): #explore every edge
            for neighbour, path_cost in zip(adj[node], cost[node]): #through neighbours of current node
                if distance[neighbour] > distance[node] + path_cost: #if current cost high then replace with new cost
                    distance[neighbour] = distance[node] + path_cost
                    reachable[neighbour] = 1 #can reach neighbour node
                
                
            
    #check if negative cycle (basically if we can lower the current calculated costs somehow)
    q = queue.Queue()
    [q.put(i) for i in range(len(adj))]
    while not q.empty():
        node = q.get()
        for neighbour, path_cost in zip(adj[node], cost[node]):
            if distance[neighbour] > distance[node] + path_cost:
                distance[neighbour] = distance[node] + path_cost
                if shortest[neighbour] == 1:
                    q.put(neighbour) #re-relax node as a current distance changed
                    shortest[neighbour] = 0
            
    


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [6,7,1,2,10,2,3,5,1,3,100,3,5,7,5,4,10,4,3,-18,6,1,-1,1]
    #data = [5,4,1,2,1,4,1,2,2,3,2,3,1,-5,4]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]-1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
