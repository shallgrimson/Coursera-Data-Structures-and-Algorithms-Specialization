'''
Problem 1 - Computing the minimum cost of a flight

Soln - Use Dijkstra's Algorithm
'''
import sys
#import queue
import heapq

#reorder heap with new distance value
def change_priority(q, node, dist):
    for i, t in enumerate(q):
        if t[1] == node:
            q[i] = (dist, node)
            
    #return heapq.heapify(q) ###########it may be faster to do this once after all neighbours have been updated
    return q


#dijkstra's algorithm
def distance(adj, cost, s, t):
    dist = [sys.maxsize]*len(adj) #store distance values
    prev = [0]*len(adj) #store previous node that led to this node
    q = [] #used to sort based on distance, use binary heap
    dist[s] = 0 #start of node
    for node in range(len(adj)):
        heapq.heappush(q, (dist[node], node)) #put nodes into heap with their current costs
        
    while len(q)>1: #since can't pop element from heap if only 1 left
        _ , min_node = heapq.heappop(q)
        for neighbour, neighbour_cost in zip(adj[min_node], cost[min_node]):
            if dist[neighbour] > dist[min_node] + neighbour_cost:
                dist[neighbour] = dist[min_node] + neighbour_cost
                prev[neighbour] = min_node
                #q.put((dist[neighbour], node)) #need to update queue
                q=change_priority(q, neighbour, dist[neighbour])
        
        heapq.heapify(q) #reorder queue
        
    #get path to final node
    # path = []
    # path.append(t)
    # cur = t
    # while cur != s:
    #     path.append(prev[cur])
    #     cur = prev[cur]
    
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    # data = [4,4,1,2,1,4,1,2,2,3,2,1,3,5,1,3]
    # data = [5,9,1,2,4,1,3,2,2,3,2,3,2,1,4,2,4,3,5,4,5,4,1,2,5,3,3,4,4,1,5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
