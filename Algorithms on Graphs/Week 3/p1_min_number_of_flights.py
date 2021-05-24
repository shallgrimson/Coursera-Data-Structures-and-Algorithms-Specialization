'''
Problem 1 - Computing the Minimum Number of Flight Segments
'''

import sys
from queue import Queue #THIS MAY HAVE TO BE CHANGED TO queue to get this to work on grader

'''
Find distance between two nodes, using breadth first search
'''
def distance(adj, s, t):
    dist = [-1 for i in range(len(adj))] #initialize distance array
    dist[s] = 0
    q = Queue()
    q.put(s)
    
    while not q.empty():
        cur = q.get() #get top of queue
        for neighbour in adj[cur]:
            if dist[neighbour] == -1: #if have not seen node before
                q.put(neighbour) #add neightbour to queue
                dist[neighbour] = dist[cur]+1 #update distance to this neighbour
    
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))