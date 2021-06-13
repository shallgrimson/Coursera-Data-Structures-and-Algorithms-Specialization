import sys

'''
Problem 1 - Maximum Amount of Gold
Set number of bars, for each bar can either take it or not
'''
def DP_max_gold(W, n, barW):
    maxWeights = [[0 for i in range(W+1)] for j in range(n+1)] #array to hold max weights at each weight
    
    barW.sort()
    for i in range(1,n+1):
        for j in range(1,W+1):
            maxWeights[i][j] = maxWeights[i-1][j] #if item is not used set to value of previous row
            wi = j-barW[i-1]
            if  wi >= 0:
                val = maxWeights[i-1][wi] + barW[i-1] #previous weight with current weight
                if val > maxWeights[i][j]:
                    maxWeights[i][j] = val

    return maxWeights[-1][-1]

'''
Problem 2 - Partitioning Souvenirs - You and two of your friends have just returned back home after visiting various countries. Now you would
like to evenly split all the souvenirs that all three of you bought.

Input - The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated
by spaces.

Output - Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
0 otherwise. 

%checks - if we reach two thrids add one
        - if final element added is equal to a third add one

%dynamic programming can do this by saving submet into dic and checking if we have already seen this subset and what the outcome will be
'''
def Partitioning_Souvenirs(n, arr):
    total = sum(arr)
    if n < 3 or total % 3:
        return 0

    third = total // 3

    #return Partitioning_recursion(arr, 0, third, third, third)
    return DP_Partitioning(arr, third, total)

#####THIS WILL BE VERY SLOW DOING RECURSION
def Partitioning_recursion(S, n, sum1, sum2, sum3):
    if sum1 == 0 and sum2 == 0 and sum3 == 0:
        return 1

    #if no items left
    if n >= len(S):
        return 0
    
    #first element in subset gets added to first set
    s1, s2, s3 = False, False, False
    if sum1 - S[n] >= 0:
        s1 = Partitioning_recursion(S, n+1, sum1-S[n], sum2, sum3)
    
    #first element in subset gets added to second set
    if sum2 - S[n] >= 0:
        s2 = Partitioning_recursion(S, n+1, sum1, sum2-S[n], sum3)

    #first element in subset gets added to third set
    if sum3-S[n] >= 0:
        s3 = Partitioning_recursion(S, n+1, sum1, sum2, sum3-S[n])
    
    return int(s1 or s2 or s3)


'''
Problem 3 - Maximum Value of an Arithmetic Expression
In this problem, your goal is to add parentheses to a given arithmetic
expression to maximize its value. 
'''
def max_arithmetic_expression(eqn):
    
    nums = []
    symb = []
    #break up expression
    for i in range(len(eqn)):
        nums.append(int(eqn[i])) if not i%2 else symb.append(eqn[i])
    
    m = [[i for i in nums] for j in nums]
    M = m
    n=len(nums)

    for s in range(0,n-2):
        for i in range(0,n-1-s):
            j = i+s
            m[i][j], M[i][j] = MinAndMax(m, M, nums, symb, i, j)

    for i in M:
        print(i)
    return M[1][n-1]

def MinAndMax(m, M, nums, symb, i, j):
    minVal = sys.maxsize
    maxVal = -(sys.maxsize)

    for k in range(i,j-1):
        
        a = getEqnValue(M[i][k], M[k+1][j], symb[k])
        b = getEqnValue(M[i][k], m[k+1][j], symb[k])
        c = getEqnValue(m[i][k], M[k+1][j], symb[k])
        d = getEqnValue(m[i][k], m[k+1][j], symb[k])
        

        minVal = min([minVal,a,b,c,d])
        maxVal = max([maxVal,a,b,c,d])
        
    return minVal,maxVal


        
def getEqnValue(a,b,sym):
    if sym == '+':
        return a+b
    if sym == '-':
        return a-b
    if sym == '*':
        return a*b
    if sym == '/':
        return a/b


if __name__ == "__main__":
    # print(DP_max_gold(10, 3, [1,4,8]))
    # print(DP_max_gold(15, 5, [1,4,2, 8, 5]))


    # print(Partitioning_Souvenirs(5, [3, 1, 1, 2, 2]))
    # print(Partitioning_Souvenirs(4, [3, 3,3,3]))
    # print(Partitioning_Souvenirs(1, [40]))
    # print(Partitioning_Souvenirs(11, [17,59,34,57,17,23,67,1,18,2,59]))
    # print(Partitioning_Souvenirs(13, [1,2,3,4,5,5,7,7,8,10,12,19,25]))

    print(max_arithmetic_expression("5-8+7*4-8+9"))    