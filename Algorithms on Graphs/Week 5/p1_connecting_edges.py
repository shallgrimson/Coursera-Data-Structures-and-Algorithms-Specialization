'''
Problem 1 - Building roads to connect cities

In this problem, the goal is to build roads between some pairs of the
given cities such that there is a path between any two cities and the
total length of the roads is minimized.

Soln: Prim's algorithm
'''

import sys
import math
import heapq

#find distances betn nodes
def get_min_distance(x, y, group, q, cur_index):
    for i in range(len(x)):
        if i != cur_index and group[i] == 0:
            #find distance btween nodes and then find the min one
            delta_x = x[i] - x[cur_index]
            delta_y = y[i] - y[cur_index]
            dis = math.sqrt(delta_x*delta_x + delta_y*delta_y)
            heapq.heappush(q, (dis, i)) #add dist to q
            
                

#main loop
def minimum_distance(n, x, y):
    result = 0.0
    group = [0 for i in range(n)] #assign groups
    q = [(0,0)]
    cnt = n #count number of iterations
    while cnt > 0: 
        cur_node = heapq.heappop(q)
        group[cur_node[1]] = 1
        result+=cur_node[0]
        get_min_distance(x, y, group, q, cur_node[1])
        cnt-=1
        
        
    return result


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    # data = [4,0,0,0,1,1,0,1,1]
    # data = [5,0,0,0,2,1,1,3,0,3,2]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(n, x, y)))
  