import sys

'''
Problem 1 - Money Change Again
Complete money change problem again but this time using dynamic programming rather than the greedy algorithm
'''

def DPChange(money, coinArr):
    MinNumCoins = [sys.maxsize for i in range(money+1)] #arry with max sizes of int
    MinNumCoins[0] = 0

    for n in range(1, money+1):
        for coin in coinArr:
            if n >= coin:
                NumCoins = MinNumCoins[n-coin]+1 #n-coin is what is important here
                if NumCoins < MinNumCoins[n]:
                    MinNumCoins[n] = NumCoins
    
    return MinNumCoins[-1]


'''
Problem 2 - Primitive Calculator
Calculator that can multiply by 2, multiply by 3 or add 1
'''

def PrimitiveCalculator(num):
    numOperations = [sys.maxsize for i in range(num+1)]
    numOperations[1] = 0
    intermediateNums = [[] for i in range(num+1)]
    intermediateNums[1] = [1]
    for i in range(2, num+1):
        for op in checkAllOperations(i): #check out of each each operation
            #mathOp = int(checkNumberOperation(i))
            numOp = numOperations[op] + 1
            if numOp < numOperations[i]:
                numOperations[i] = numOp
                intermediateNums[i] = intermediateNums[op] + [i]


    return numOperations[num], intermediateNums[num]

#this qay may be slow so could probably hard code it
def checkAllOperations(num):
    op = []

    if num%3 == 0:
        op.append(int(num/3))

    if num%2 == 0:
        op.append(int(num/2))
    
    op.append(num-1)

    return op


'''
Problem 3 - Edit Distance - this is that string problem but goal is to implement the edit distance
*****CURRENTLY ASSUMING ALL LOWER CASE BUT COULD CHANGE THIS*****
i-row
j-col

I edited a bit of the code base on https://www.geeksforgeeks.org/edit-distance-dp-5/, but seems to be right
NOTE THAT DIRECTION IS NOT REALLY NEEDED FOR THIS BUT CAN BE USED TO DISPLAY INSERTION, DELETION AND WHAT NOT

ALOS CAN COMBINE ALL CODE INTO ONE FUNCTION
'''
def editDistance(A, B):
    #don't need cost array, can just find 
    cost = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)] #holds costs
    #direction = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)] #direction from which they were found
    cost[0] = [j for j in range(len(B)+1)] # THIS CAN BE REMOVED AND MOVED UPWARDS AS DOESN'T MATTER IF I+1 OR J+1 OR ZERO OR 1000, THEY ARE NOT LOOKED AT
    #direction[0] = [3 for j in range(len(B)+1)]

    for i in range(len(A)+1):
        cost[i][0] = i
     #   direction[i][0] = 4

    for i in range(1,len(A)+1): #row
        for j in range(1,len(B)+1): #col
            #cost[i][j], direction[i][j] = findCostandDirection(cost, i, j, A[i-1]==B[j-1])
            cost[i][j] = findCostandDirection(cost, i, j, A[i-1]==B[j-1])
            

    #return findEditDistance(direction, len(A), len(B)) #currently just find the edit distance
    return cost[len(A)][len(B)]

#match - direction = 1
#mismatch - direction = 2
#insetion - direction = 3
#deletion - direction 4
def findCostandDirection(cost, i, j, same):
    if same: #match, if letters equal 
        D1 = cost[i-1][j-1]
        #direction = 1
        #return D1, direction #is this right though based on the previous elements?
        return D1

    else: #mismatch, if letters are not
        D1 = cost[i-1][j-1]+1
        #direction = 2

    D2 = cost[i][j-1]+1 #insertion
    D3 = cost[i-1][j]+1 #deletion

    return min(min(D1, D2), D3)
    # D = D1
    # if D2 < D1:
    #     D = D2
    #     direction = 3
        
    # if D3 < D2:
    #     D = D3
    #     direction = 4

    # return D, direction


#find the edit distance from the distance array
# def findEditDistance(direction, i, j):
#     editDist = 0
#     while i != 1 and j != 1: #NOTE SURE ABOUT THE 1 AND 1
#         if direction[i][j] == 3 or direction[i][j] == 4:
#             i -= 1
#             j -= 1
#             editDist += 1
#         elif direction[i][j] == 2:
#             j-=1
#         elif direction[i][j] == 1:
#             i-=1
    
#     return editDist
        
'''
PROBLEM 4 - Longest Common Subsequence of Two Sequences
Compute the length of a longest common subsequence of three sequences.
'''
def longestSubsequence(lenA, A, lenB, B):
    cost = [[0 for j in range(lenB+1)] for i in range(lenA+1)] #holds costs

    for i in range(1,lenA+1): #row
        for j in range(1,lenB+1): #col
            if A[i-1]==B[j-1]:
                cost[i][j] = cost[i-1][j-1]+1 #opposite of alignment game
            else:
                cost[i][j] = max(cost[i-1][j], cost[i-1][j-1]) #opposite of alignment game
    
    return cost[lenA][lenB]

'''
PROBLEM 5 - Longest Common Subsequence of Three Sequences
-can use 3d array to solve and just modify the above code
- find all sub strings and then see if they exist in the third array
'''
# def ThreelongestSubsequence(lenA, A, lenB, B, lenC, C):
#     cost = [[[0 for j in range(lenB+1)] for i in range(lenA+1)] for k in range(lenC+1)] #holds costs

#     for k in range(1,lenC+1):
#         for i in range(1,lenA+1): #row
#             for j in range(1,lenB+1): #col
#                 if A[i-1]==B[j-1]:
#                     cost[i][j] = cost[i-1][j-1]+1 #opposite of alignment game
#                 else:
#                     cost[i][j] = max(cost[i-1][j], cost[i-1][j-1]) #opposite of alignment game
    
#     return cost[lenA][lenB]

if __name__ == "__main__":
    #print(DPChange(8, [1,3,4]))

    #print(PrimitiveCalculator(5))
    #print(PrimitiveCalculator(96234))

    ##########################
    # print(editDistance("ab", "ab"))
    # print(editDistance("short", "ports"))
    # print(editDistance("editing", "distance"))
    # print(editDistance("sunday", "saturday")) # this should be 3
    # print(editDistance("kitten", "sitting")) # this should be 3
    # print(editDistance("horse", "ros")) # this should be 3
    ##########################

    print(longestSubsequence(3, [2,7,5], 2, [2,5])) 
    print(longestSubsequence(1, [7], 4, [1,2,3,4])) 
    print(longestSubsequence(4, [2,7,8,3], 4, [5,2,8,7])) 
    print(longestSubsequence(5, [2,5,2,7,5], 3, [2,7,5])) 
 