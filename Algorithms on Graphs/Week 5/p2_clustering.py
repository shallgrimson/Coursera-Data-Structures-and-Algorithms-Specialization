'''
Problem 2 - Clustering

Clustering is a fundamental problem in data mining. The goal is to partition
a given set of objects into subsets (or clusters) in such a way that any two
objects from the same subset are close (or similar) to each other, while any
two objects from different subsets are far apart.

I.e create k sets of maximum distance apart
Refer to https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/ for algorthim overview
'''



import sys
import math
def find(parent, u):
    #print(parent[u],u)
    while parent[u] != u:
        u = parent[u]
    return u

def union(rank, parent, u, v): #just arbitraily choose rank 
    upar = find(parent, u)
    vpar = find(parent, v)
    
    if rank[vpar] > rank[upar]:
        parent[upar] = vpar
    elif rank[vpar] < rank[upar]:
        parent[vpar] = upar
    else: 
        parent[upar] = vpar #arbitrarely pick parent
        rank[vpar] +=1

def clustering(n, x, y, k):
    #get costs
    costs = []
    distances = []
    for i in range(n):
        for j in range(n):
            delta_x = x[i] - x[j]
            delta_y = y[i] - y[j]
            delta = math.sqrt(delta_x*delta_x + delta_y*delta_y)
            distances.append(delta)
            if i != j:
                costs.append((delta, i, j)) #could just use distances and remove leading 0's
    
    #sort costs
    costs.sort(key=lambda x: x[0])
    parent = [] #keep track of which group each node belongs to
    rank = [] #keep track of tree size
    for i in range(n):
        parent.append(i)
        rank.append(0)

    edge_num = 0
    cnt=0
    while edge_num < n-k:
        _, u, v = costs[cnt]
        cnt+=1
        g1 = find(parent, u)
        g2 = find(parent, v)

        if g1 != g2:
            edge_num +=1 #add edge
            union(rank, parent, u, v)
    
    
    #find distance between groups
    groups = [find(parent, i) for i in range(n)] #organize into groups
    min_dist = 1001
    for i in range(n):
        for j in range(n):
            if groups[i] != groups[j]:
                # delta_x = x[i] - x[j]
                # delta_y = y[i] - y[j]
                # delta = math.sqrt(delta_x*delta_x + delta_y*delta_y)
                if min_dist > distances[i*(n)+j]:
                    min_dist = distances[i*(n)+j]

        
    return min_dist


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    #data = [12,7,6, 4,3, 5,1, 1,7, 2,7, 5,7, 3,3, 7,8, 2,8, 4,4, 6,7, 2,6 ,3]
    #data=[8,3,1,1,2,4,6,9,8,9,9,8,9,3,11,4,12,4]
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(n, x, y, k)))
    
