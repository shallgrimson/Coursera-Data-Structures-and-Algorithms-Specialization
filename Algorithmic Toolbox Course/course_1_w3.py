'''
Problem 1 - basic greedy algorithm - in the problem values is hardcoded to [1,5,10]
'''
def basic_greedy_alg(values, amount):
    values.sort(reverse=True)
    cnt = 0

    for i_val in values:
        if i_val <= amount:
            cnt = cnt + int(amount/i_val)
            amount = amount%i_val
        
        if amount == 0:
            break
    
    return cnt


'''
Problem 2 - Find the most valuable combination
of items assuming that any fraction of a loot item can be put into his bag.

W is inputted as [[value_1, weight_1], [value_2, weight_2], ...]
'''
def sort_key(e):
    return e[0]/e[1] #value / weight

def fractional_knapsack(num_items, knapsack_W, items):
    items.sort(key=sort_key, reverse=True) #it may be fasted to just find the item each time but I don't think it would be averall
    knapsack_Value = 0.0

    for max_item in items:
        if knapsack_W <= 0:
            break
        
        amount = knapsack_W/max_item[1]
        amount = min(amount, 1) #either take full or patrial bit of item
        print(amount)
        knapsack_W = knapsack_W - amount*max_item[1]

        knapsack_Value = knapsack_Value + amount*max_item[0]
    
    return knapsack_Value


'''
Problem 3 - Car Fueling
d - city d miles away
m - how many miles the car can travel on a full tank
n - number of available stops
stops - array contain distances of each stop
'''
def car_fueling(d, m, n, stops):
    mileage = m
    cur_stop = 0
    cnt_stops = 0
    stops.append(d) 

    for next_stop in stops:
        delta_dist = next_stop - cur_stop
        if delta_dist > m:
            return -1

        if delta_dist <= mileage: #check if can get to next stop on current tank
            mileage = mileage - delta_dist
        else: #refill at current stop
            cnt_stops = cnt_stops + 1
            mileage = m - delta_dist
        
        cur_stop = next_stop #drive to this stop

        
    return cnt_stops

'''
Problem 4 - Maximum Avertisement Revenue
'''
def max_ad_revenue(n, clicks, rev):
    clicks.sort(reverse=True)
    rev.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum = sum + clicks[i]*rev[i]
    
    return sum

'''
Problem 5 - Collecting Signatures
You are responsible for collecting signatures from all tenants of a certain building. For each tenant, you know a period of time when he or she is at home.
You would like to collect all signatures by visiting the building as few times as
possible
'''
def segment_key(e): #sort based on end points
    return e[1]

def find_min_points(n, segmentArray):
    segmentArray.sort(key=segment_key)
    endPoint = -1
    pointsArray = []
    for segment in segmentArray:
        if segment[0] > endPoint:
            endPoint = segment[1]
            pointsArray.append(endPoint)
    
    return(pointsArray)
        

'''
Problem  - Maximum Number of Prizes
Basically input integet split it up into the maximum amount of unique integers
'''
def max_num_prizes(num):
    if num == 0:
        return 0

    prizeSplit = []
    curSum, prevSum = 0, 0 #count number of prizes already split up

    for i in range(1, num+1):
        curSum = curSum + i
        if num - curSum <= i:
            prizeSplit.append(num-prevSum)
            return prizeSplit

        prizeSplit.append(i)
        prevSum = curSum



if __name__ == "__main__":
    #print(fractional_knapsack(3,50,[[60,20],[100,50],[120,30]]))
    #print(fractional_knapsack(1,10,[[500, 30]]))

    # print(car_fueling(10, 3, 4, [1,2,5,9]))
    # print(car_fueling(950, 400, 4, [200,375,550,750]))

    # print(max_ad_revenue(1,[23],[39]))
    # print(max_ad_revenue(3,[1,3,-5],[-2,4,1]))

    #print(find_min_points(3, [[1,3],[2,5], [3,6]]))
    #print(find_min_points(4, [[4,7], [1,3], [2,5], [5,6]]))
    #print(find_min_points(4, [[1,17], [4,9], [1,5], [5,7], [12, 14], [8, 12], [8,14], [3,9], [7, 10], [16,19]]))

    print(max_num_prizes(12))