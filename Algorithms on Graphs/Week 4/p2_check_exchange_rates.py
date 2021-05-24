'''
Problem 3 - Detecting Anomalies in Currency Exchange Rates
'''
import sys

def negative_cycle(adj, cost):
    rates = [sys.maxsize]*len(adj) #store distance values
    rates[0] = 0 #just start at node 0
    
    #run through distances once
    for node in range(len(adj)):
        for neighbour, path_cost in zip(adj[node], cost[node]): #through neighbours of current node
            if rates[neighbour] > rates[node] + path_cost: #if current cost high then replace with new cost
                rates[neighbour] = rates[node] + path_cost
    
    #check if negative cycle (basically if we can lower the current costs somehow)
    for node in range(len(adj)):
        for neighbour, path_cost in zip(adj[node], cost[node]):
            if rates[neighbour] > rates[node] + path_cost:
                return 1
            
    return 0



if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        
    print(negative_cycle(adj, cost))
    
